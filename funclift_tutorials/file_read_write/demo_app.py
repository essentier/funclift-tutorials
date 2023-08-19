from mock_interpreter import TextFileOpToMock
from dsl import Read, Write
from funclift.fp.monad_runner import run_monads
from io_interpreter import TextFileOpToIO

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


option_effect = program.foldmap(TextFileOpToMock())
print(option_effect)