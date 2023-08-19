# x = input('enter a number: ')
# print(x)

from funclift.types.writer import LogWriter, Writer
from funclift.fp.curry import curry

def get_number_with_log(n: int) -> Writer[list[str], int]:
    return LogWriter.pure2(n, [f'got number {n}'])

@curry
def sum(a: int, b: int) -> bool:
    return a + b

def is_even(n: int) -> bool:
    return n % 2 == 0

def log_is_even(b: bool) -> Writer[list[str], bool]:
    return LogWriter.pure2(b, [f'sum is even: {b}'])

num1 = get_number_with_log(5)
num2 = get_number_with_log(3)
num = LogWriter.pure(sum).ap(num1).ap(num2)
num_even = num.fmap(is_even)
num_even_logged = num_even.flatmap(log_is_even)
print(num_even_logged)

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

# get_number() \
#     .fmap(sum) \
#     .ap(get_number()) \
#     .fmap(is_even) \
#     .flatmap(print_result) \
#     .unsafe_run()

# from funclift.fp.monad_runner import run_monads

# def create_program_monads():
#     num1 = yield get_number()
#     num2 = yield get_number()
#     num = sum(num1, num2)
#     num_even = is_even(num)
#     _ = yield print_result(num_even)
#     return IO.pure(None)

# monads = create_program_monads()
# program = run_monads(monads)
# program.unsafe_run()

