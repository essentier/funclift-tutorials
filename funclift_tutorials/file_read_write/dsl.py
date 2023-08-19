from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar
from funclift.free_monad import Free

A = TypeVar('A')


class TextFileOp(ABC, Generic[A]):
    def lift(self) -> Free[TextFileOp, A]:
        return Free.liftm(self)


@dataclass
class Read(TextFileOp[str]):
    filename: str


@dataclass
class Write(TextFileOp[None]):
    filename: str
    text: str
