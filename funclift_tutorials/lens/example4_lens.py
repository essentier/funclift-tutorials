from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Generic, Protocol, TypeVar, Tuple
from profunctor import Strong, Profunctor
from forget import Forget

# A lens has the type p a b -> p s t
# The type says that given a way to go from a to b (i.e. p a b)
# a lens will give us a way to go from s to t (i.e. p s t)
# p is a profunctor.

A = TypeVar('A', contravariant=True)
B = TypeVar('B')
S = TypeVar('S', covariant=True)
T = TypeVar('T')
S1 = TypeVar('S1', covariant=True)
T1 = TypeVar('T1')
C = TypeVar('C')
D = TypeVar('D')
R = TypeVar('R')
P = TypeVar('P')
X = TypeVar('X')



@dataclass
class Func(Generic[B, C]):
    func: Callable[[B], C]

    def __call__(self, b: B) -> C:
        return self.func(b)

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

# _1 in the original example
# get_first is like a lens.
# It takes Forget r a d and essentially returns Forget r (a d) (c d)
# c, (c d) are not used
def on_first(p: Strong[P, B, C]) -> Strong[P, Tuple[B, D], Tuple[C, D]]:
    return p.first()

# id_forget is a profunctor
id_forget = Forget(lambda x: x)

# actions
def view(_lens: Lens, s: S) -> T:
    return _lens(id_forget)(s)

def set(_lens: Lens, b: B, s: S) -> T:
    return _lens(Func(lambda x: b))(s)

# helper
# def lens(s -> a, s -> b -> t) -> Lens p s t a b
# def lens(getter: Callable[[S], A], setter: Callable[[S, B], T]) -> Lens[P, S, T, A, B]:
#     ...

def lens1(getter: Callable[[S], A], setter: Callable[[S, B], T], pab: Strong[P, A, B]) -> Strong[P, S, T]:
    def dup(x):
        return (x, x)
    
    def something(px_bs: Profunctor[P, X, Tuple[B, S]]) -> Profunctor[P, X, T]:
        return px_bs.rmap(lambda bs: setter(bs[1], bs[0]))
    
    # def func(s: S):
    #     return something(pab.lmap(getter).first(dup(s)))
    
    return something(pab.lmap(getter).lmap(dup).first())

def lens(getter: Callable[[S], A], setter: Callable[[S, B], T]) -> Lens[P, A, B, S, T]:
    def dup(x):
        return (x, x)
    
    def something(px_bs: Profunctor[P, X, Tuple[B, S]]) -> Profunctor[P, X, T]:
        return px_bs.rmap(lambda bs: setter(bs[1], bs[0]))
    
    def func(pab: Strong[P, A, B]):
        return something(pab.lmap(getter).first().lmap(dup))
    
    return func

on_first2 = lens(lambda ab: ab[0], lambda ac, b: (b, ac[1]))
# examples

def compose(lens1: Lens[P, A, B, S1, T1], lens2: Lens[P, S1, T1, S, T]) -> Lens[P, A, B, S, T]:
    def f(pab: Strong[P, A, B]) -> Strong[P, S, T]:
        return lens2(lens1(pab))
    return f

if __name__ == "__main__":
    result = on_first(id_forget)((5, 'hi'))
    print(result)

    result = view(on_first, (5, 'hi'))
    print(result)

    result = set(on_first, 12, (5, 'hi'))
    print(result)

    result = set(on_first, 12, ((5, 'oh'), 'hi'))
    print(result)

    result = set(compose(on_first, on_first), 12, ((5, 'oh'), 'hi'))
    print(result)

    result = view(on_first2, (5, 'hi'))
    print(result)

    result = set(on_first2, 12, (5, 'hi'))
    print(result)
