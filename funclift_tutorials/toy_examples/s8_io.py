# x = input('enter a number: ')
# print(x)

from funclift.types.io import IO
from funclift.fp.curry import curry

def get_number() -> IO[int]:
    return IO(lambda: int(input('enter a number: ')))

@curry
def sum(a: int, b: int) -> bool:
    return a + b

def is_even(n: int) -> bool:
    return n % 2 == 0

def print_result(num_even: bool) -> IO[None]:
    return IO(lambda: print('is even: ', num_even))

num1 = get_number()
num2 = get_number()
num = IO.pure(sum).ap(num1).ap(num2)
num_even = num.fmap(is_even)
program = num_even.flatmap(print_result)
program.unsafe_run()

# get_number() \
#     .fmap(is_even) \
#     .flatmap(print_result) \
#     .unsafe_run()

# IO.pure(sum) \
#     .ap(get_number()) \
#     .ap(get_number()) \
#     .fmap(is_even) \
#     .flatmap(print_result) \
#     .unsafe_run()

get_number() \
    .fmap(sum) \
    .ap(get_number()) \
    .fmap(is_even) \
    .flatmap(print_result) \
    .unsafe_run()

from funclift.fp.monad_runner import run_monads

def create_program_monads():
    num1 = yield get_number()
    num2 = yield get_number()
    num = sum(num1, num2)
    num_even = is_even(num)
    _ = yield print_result(num_even)
    return IO.pure(None)

monads = create_program_monads()
program = run_monads(monads)
program.unsafe_run()

