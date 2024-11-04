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
S1 = TypeVar('S1', covariant=True)
T1 = TypeVar('T1')
C = TypeVar('C')
D = TypeVar('D')
R = TypeVar('R')
P = TypeVar('P')
X = TypeVar('X')


# Forget r is like a profunctor
@dataclass
class Forget(Generic[R, B, C]):
    b_to_r: Callable[[B], R]

    def __call__(self, b: B) -> R:
        return self.b_to_r(b)

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

    # def left(self) -> Forget[R, Either[A, C], Either[B, C]]:

    def lmap(self, f: Callable[[A], B]) -> Profunctor[P, A, C]:
        return self.dimap(f, lambda x: x)

    def rmap(self, g: Callable[[C], D]) -> Profunctor[P, B, D]:
        return self.dimap(lambda x: x, g)
