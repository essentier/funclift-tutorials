from functools import singledispatch
from typing import Any, TypeVar
from funclift.types.io import IO, io_effect
from funclift.fp.monad_runner import run_monads
from textfile_dsl import TextFileOp, Read, Write

A = TypeVar('A')


class TextFileIO():

    @singledispatch
    @staticmethod
    def create_effect(op: TextFileOp[A]) -> Any: ...

    @create_effect.register
    @staticmethod
    @io_effect
    def read_effect(op: Read) -> str:
        with open(op.filename, "r") as file:
            return file.read()

    @create_effect.register
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
        return TextFileIO.create_effect(op)


def create_app_dsl():
    filename = 'hello.txt'
    _ = yield Write(filename, 'Hello PyCon Latam').lift()
    contents = yield Read(filename).lift()
    return contents


app_dsl = create_app_dsl()
program = run_monads(app_dsl)
io_effects = program.foldmap(TextFileOpToIO())
content = io_effects.unsafe_run()
print(content)