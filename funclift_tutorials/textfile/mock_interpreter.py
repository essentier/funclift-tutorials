from typing import TypeVar
from dsl import TextFileOp, Read, Write
from functools import wraps
from funclift.types.id import Id

A = TypeVar('A')


def id_effect(func):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Id[A]:
        return Id(func(*args, **kwargs))

    return wrapper


class TextFileMock():
    contentsMap: dict[str, str] = {}

    @staticmethod
    @id_effect
    def read_effect(op: Read) -> str:
        return TextFileMock.contentsMap[op.filename]

    @staticmethod
    @id_effect
    def write_effect(op: Write) -> None: 
        TextFileMock.contentsMap[op.filename] = op.text

# natural transformation that maps TextFileOp[A] to IO[A]
class TextFileOpToMock():
    def mempty(self, a: A) -> Id[A]:
        return Id.pure(a)

    def apply(self, op: TextFileOp[A]) -> Id[A]:
        match op:
            case Read():
                return TextFileMock.read_effect(op)
            case Write():
                return TextFileMock.write_effect(op)


