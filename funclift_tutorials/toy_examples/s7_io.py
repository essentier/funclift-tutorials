# x = input('enter a number: ')
# print(x)

from funclift.types.io import IO

def get_number() -> IO[int]:
    return IO(lambda: int(input('enter a number: ')))

def is_even(n: int) -> bool:
    return n % 2 == 0

def print_result(num_even: bool) -> IO[None]:
    return IO(lambda: print('You entered an even number: ', num_even))

# num = get_number()
# num_even = num.fmap(is_even)
# program = num_even.flatmap(print_result)
# program.unsafe_run()

get_number() \
    .fmap(is_even) \
    .flatmap(print_result) \
    .unsafe_run()

from funclift.fp.monad_runner import run_monads

def create_program_monads():
    num = yield get_number()
    num_even = is_even(num)
    _ = yield print_result(num_even)
    return IO.pure(None)

# monads = create_program_monads()
# program = run_monads(monads)
# program.unsafe_run()

# y = IO(lambda: input('enter another number: '))
