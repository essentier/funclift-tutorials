print('traversable example')

from typing import Iterator, TypeVar, Callable
from funclift.applicative import Applicative
from funclift.functor import Functor

AP = TypeVar('AP', bound=Applicative)
F = TypeVar('F', bound=Functor)
A = TypeVar('A')
B = TypeVar('B')
AP_IB = Applicative[AP, Iterator[B]]

# make iterator traversable
# iterator needs to be a functor and foldable

class IteratorTraversable:

    # traverse  :: Applicative f => (a -> f b) -> t a -> f (t b)
    @staticmethod
    def traverse(ta: Iterator[A], f: Callable[[A], Applicative[AP, B]]) -> AP_IB:
        a = next(ta)
        ap_b = f(a)
        ap_ib = IteratorTraversable.traverse(ta, f)
        


    # sequenceA :: Applicative f => t (f a) -> f (t a)
