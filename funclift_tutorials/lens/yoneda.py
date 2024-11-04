# newtype Yoneda f a = Yoneda { runYoneda :: forall b. (a -> b) -> f b }

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Generic, Protocol, TypeVar, Tuple
from funclift.functor import Functor
import logging

log = logging.getLogger(__name__)

A = TypeVar('A', covariant=True)
B = TypeVar('B', covariant=True)
C = TypeVar('C', covariant=True)
F = TypeVar('F')
D = TypeVar('D')
P = TypeVar('P', covariant=True)


@dataclass
class Yoneda(Generic[F, A]):
    """Yoneda"""

    # forall b. (a -> b) -> f b
    _nt: Callable[[Callable[[A], B]], Functor[F, B]]

    def __call__(self, f: Callable[[A], B]) -> Functor[F, B]:
        return self._nt(f)

    @staticmethod
    def lift(functor: Functor[F, A]) -> Yoneda[F, A]:
        """lift Yoneda
        """
        def _f(a2b: Callable[[A], B]) -> Functor[F, B]:
            return functor.fmap(a2b)
        
        return Yoneda(_f)
    
    @staticmethod
    def lower(y: Yoneda[F, A]) -> Functor[F, A]:
        y._nt(lambda x: x)


# examples
