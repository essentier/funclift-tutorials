from __future__ import annotations
from abc import abstractmethod
from dataclasses import dataclass
from typing import Callable, Generic, Protocol, TypeVar
from funclift.functor import Functor
import logging

log = logging.getLogger(__name__)

A = TypeVar("A", contravariant=True)
B = TypeVar("B")
F = TypeVar("F")


# class Comonad(Functor[F, A], Protocol):
#     @staticmethod
#     def counit(a: A) -> Comonad[F, A]:
#         ...

#     # @abstractmethod
#     # def cojoin():
#     #     ...

#     @abstractmethod
#     def coflatmap(self, f: Callable[[Comonad[F, A]], B]) -> Comonad[F, B]:
#         ...


class Stream():
    ...


@dataclass
class StreamZipper(Generic[A]):
    left: Stream[A]
    focus: A
    right: Stream[A]

    def move_left(self) -> StreamZipper[A]:
        # return new StreamZipper(self.left.tail, self.left.head, focus)
        ...
    
    def move_right(self) -> StreamZipper[A]:
        ...