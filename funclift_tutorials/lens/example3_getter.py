from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Generic, Protocol, TypeVar, Tuple
from profunctor import Strong

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

# Getter is like a lens where the profunctor p is Forget r
Getter = Callable[[Forget[B, B, C]], Forget[B, S, T]]

# _1 in the original example
# get_first is like a lens.
# It takes Forget r a d and essentially returns Forget r (a d) (c d)
# c, (c d) are not used
def get_first(p: Strong[B, C]) -> Strong[Tuple[B, D], Tuple[C, D]]:
    return p.first()


id_forget = Forget(lambda x: x)

# actions
def view(getter: Getter, s: S) -> T:
    return getter(id_forget).b_to_r(s)


# examples

if __name__ == "__main__":
    result = get_first(id_forget).b_to_r((5, 'hi'))
    print(result)

    result = view(get_first, (5, 'hi'))
    print(result)
