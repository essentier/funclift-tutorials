
# Lenses, Prisms and Optics in Scala | Rock the JVM
# https://www.youtube.com/watch?v=a09aBGccUTE

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Generic, Protocol, TypeVar, Tuple
from profunctor import Strong, Profunctor

# A lens has the type p a b -> p s t
# The type says that given a way to go from a to b (i.e. p a b)
# a lens will give us a way to go from s to t (i.e. p s t)
# p is a profunctor.

A = TypeVar('A', contravariant=True)
B = TypeVar('B')
S = TypeVar('S', covariant=True)
T = TypeVar('T')
C = TypeVar('C')
D = TypeVar('D')
R = TypeVar('R')
P = TypeVar('P')
X = TypeVar('X')

# Forget r is like a profunctor
@dataclass
class Forget(Generic[R, B, C]):
    b_to_r: Callable[[B], R]

    # g, C, D are not used
    def dimap(self, f: Callable[[A], B],
              g: Callable[[C], D]) -> Forget[R, A, D]:
        def a_to_r(a: A) -> R:
            return self.b_to_r(f(a))
        
        return Forget(a_to_r)
    
    def first(self) -> Forget[R, Tuple[B, D], Tuple[C, D]]:
        def bd_to_r(bd: Tuple[B, D]) -> R:
            return self.b_to_r(bd[0])
        return Forget(bd_to_r)

    def lmap(self, f: Callable[[A], B]) -> Profunctor[P, A, C]:
        return self.dimap(f, lambda x: x)

    def rmap(self, g: Callable[[C], D]) -> Profunctor[P, B, D]:
        return self.dimap(lambda x: x, g)


@dataclass
class Func(Generic[B, C]):
    func: Callable[[B], C]

    def dimap(self, before: Callable[[A], B],
              after: Callable[[C], D]) -> Func[A, D]:
        def new_func(a: A) -> D:
            return after(self.func(before(a)))
        
        return Func(new_func)
    
    def first(self) -> Func[Tuple[B, D], Tuple[C, D]]:
        def new_func(bd: Tuple[B, D]) -> Tuple[C, D]:
            return self.func(bd[0]), bd[1]
        return Func(new_func)

    def lmap(self, f: Callable[[A], B]) -> Profunctor[P, A, C]:
        return self.dimap(f, lambda x: x)

    def rmap(self, g: Callable[[C], D]) -> Profunctor[P, B, D]:
        return self.dimap(lambda x: x, g)


# Getter is like a lens where the profunctor p is Forget r
# Getter = Callable[[Forget[B, B, C]], Forget[B, S, T]]
# Setter = Callable[[Callable[[A], B]], Callable[[S], T]]
Lens = Callable[[Strong[P, A, B]], Strong[P, S, T]]

id_forget = Forget(lambda x: x)

# actions
def view(getter: Lens, s: S) -> T:
    return getter(id_forget).b_to_r(s)

def set(setter: Lens, b: B, s: S) -> T:
    return setter(Func(lambda x: b)).func(s)

def lens(getter: Callable[[S], A], setter: Callable[[S, B], T]) -> Lens[P, A, B, S, T]:
    def dup(x):
        return (x, x)
    
    def something(px_bs: Profunctor[P, X, Tuple[B, S]]) -> Profunctor[P, X, T]:
        return px_bs.rmap(lambda bs: setter(bs[1], bs[0]))
    
    def func(pab: Strong[P, A, B]):
        return something(pab.lmap(getter).first().lmap(dup))
    
    return func


@dataclass
class Guitar:
    make: str
    model: str


@dataclass
class Guitarist:
    name: str
    favorite_guitar: Guitar
    
@dataclass
class RockBand:
    name: str
    year_formed: int
    lead_guitarist: Guitarist

on_first2 = lens(lambda ab: ab[0], lambda ac, b: (b, ac[1]))
# examples



if __name__ == "__main__":
    result = view(on_first2, (5, 'hi'))
    print(result)

    result = set(on_first2, 12, (5, 'hi'))
    print(result)
