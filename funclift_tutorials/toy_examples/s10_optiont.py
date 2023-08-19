from funclift.types.io import IO
from funclift.types.option import Option, Some, Nothing
from funclift.types.optiont import OptionT
from funclift.fp.curry import curry
from funclift.fp.monad_runner import run_monads

# def get_number() -> Option[int]:
#     try:
#         num = int(input('enter a number: '))
#         return Some(num)
#     except ValueError:
#         return Nothing()
    
# def get_number() -> IO[int]:
#     return IO(lambda: int(input('enter a number: ')))

def get_number_io() -> IO[str]:
    return IO(lambda: input('enter a number: '))

def create_program_monads() -> OptionT[IO, int]:
    num_str = yield OptionT.lift(get_number_io())
    try:
        num = int(num_str)
        return Some(num)
    except ValueError:
        return Nothing()

# def get_number_io() -> IO[Option[int]]:
#     return IO(lambda: get_number())



# num = get_number()
# print(num)

monads = create_program_monads()
program = run_monads(monads)
result = program.run().unsafe_run()
print(result)
