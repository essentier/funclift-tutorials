from __future__ import annotations
from typing import Callable, Generic, Protocol, TypeVar, Tuple
from funclift.types.option import Some

from funclift.functor import Functor

# A lens has the type p a b -> p s t
# The type says that given a way to go from a to b (i.e. p a b)
# a lens will give us a way to go from s to t (i.e. p s t)
# p is a profunctor.

A = TypeVar('A', covariant=True)
B = TypeVar('B', covariant=True)
S = TypeVar('S', covariant=True)
T = TypeVar('T')
C = TypeVar('C')

# Setter is a "wanna-be" lens where p is ->
# Eventually for -> to be a profunctor, we will need to implement dimap for ->.
# For now, -> is not a profunctor yet.
Setter = Callable[[Callable[[A], B]], Callable[[S], T]]
# class Setter(Generic[S, T, A, B]):
#     pass

# _1 in the original example
# set_first is like a lens.
# It takes -> a b and essentially returns -> (a c) (b c)
def set_first(f: Callable([A], B), s: Tuple[A, C]) -> Tuple[B, C]:
    return f(s[0]), s[1]

# mapped is a like a lens.
# It takes -> a b and essentially returns -> (f a) (f b).
# Here f is a functor.
def mapped(f: Callable([A], B), fa: Functor[A]) -> Functor[B]:
    return fa.fmap(f)


# actions
def over(setter: Setter, f: Callable([A], B), s: S) -> T:
    return setter(f, s)

def set(setter: Setter, b: B, s: S) -> T:
    return setter(lambda x: b, s)


# examples
def add1(a: int) -> int:
    return a + 1

if __name__ == "__main__":
    result = set_first(add1, (5, 'hi'))
    print(result)

    result = over(set_first, add1, (5, 'hi'))
    print(result)

    result = set(set_first, 12, (5, 'hi'))
    print(result)

    result = mapped(add1, Some(5))
    print(result)

    result = over(mapped, add1, Some(5))
    print(result)

    result = set(mapped, 12, Some(5))
    print(result)
