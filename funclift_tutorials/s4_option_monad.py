# def validate_name(name: str) -> Option

from dataclasses import dataclass
from funclift.types.io import IO
from funclift.fp.monad_runner import run_monads

@dataclass
class User:
    name: str

@dataclass
class Order:
    user: User
    total: int


def get_user(name: str) -> IO[User]:
    return IO.pure(User(name))


def get_order(user: User) -> IO[Order]:
    return IO.pure(Order(user, 100))


# does not compose
# order = get_order(get_user('Katy'))
# print(order.unsafe_run())

def create_program():
    user = yield get_user('Katy')
    order = yield get_order(user)
    return order

program = create_program()
app = run_monads(program)
order = app.unsafe_run()
print(order)
