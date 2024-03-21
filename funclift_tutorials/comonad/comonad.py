from __future__ import annotations
from abc import abstractmethod
from typing import Callable, Protocol, TypeVar
from funclift.functor import Functor

import logging

log = logging.getLogger(__name__)

# A = TypeVar("A", contravariant=True)
A = TypeVar("A")
B = TypeVar("B")
F = TypeVar("F")


class Comonad(Functor[F, A], Protocol):
    
    @abstractmethod
    def extract(self) -> A:
        ...

    @abstractmethod
    def duplicate(self) -> Comonad[F, Comonad[F, A]]:
        ...

    @abstractmethod
    def extend(self, f: Callable[[Comonad[F, A]], B]) -> Comonad[F, B]:
        ...

