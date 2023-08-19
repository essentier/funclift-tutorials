from typing import TypeVar
from funclift.types.io import IO, io_effect
from dsl import TextFileOp, Read, Write

A = TypeVar('A')


class TextFileIO:

    @staticmethod
    @io_effect
    def read_effect(op: Read) -> str:
        with open(op.filename, "r") as file:
            return file.read()

    @staticmethod
    @io_effect
    def write_effect(op: Write) -> None: 
        with open(op.filename, "w") as file:
            file.write(op.text)


# natural transformation that maps TextFileOp[A] to IO[A]
class TextFileOpToIO():
    def mempty(self, a: A) -> IO[A]:
        return IO.pure(a)

    def apply(self, op: TextFileOp[A]) -> IO[A]:
        match op:
            case Read():
                return TextFileIO.read_effect(op)
            case Write():
                return TextFileIO.write_effect(op)


