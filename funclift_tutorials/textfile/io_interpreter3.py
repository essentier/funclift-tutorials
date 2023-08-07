from typing import TypeVar
from funclift.types.io import IO, io_effect
from funclift.fp.monad_runner import run_monads
from textfile_dsl import TextFileOp, Read, Write

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


def create_app_dsl():
    filename = 'hello.txt'
    _ = yield Write(filename, 'Hello PyCon Latam 2023').lift()
    contents = yield Read(filename).lift()
    return contents


app_dsl = create_app_dsl()
program = run_monads(app_dsl)
io_effects = program.foldmap(TextFileOpToIO())
content = io_effects.unsafe_run()
print(content)