from funclift.types.option import Option, Nothing, Some
from funclift.fp.curry import curry

def ten_mod_by(n: int) -> Option[int]:
    if n == 0:
        return Nothing()
    
    return Some(10 % n)


# print(ten_mod_by(4))
# print(ten_mod_by(1))
# print(ten_mod_by(0))

def remainder_in_text(r: int) -> str:
    return 'remainder is ' + str(r)

def ten_mod_by_in_text(x: int) -> Option[str]:
    r = ten_mod_by(x)
    return r.fmap(remainder_in_text)

# print(ten_mod_by_in_text(4))
# print(ten_modin_by_in_text(0))

@curry
def sum(a: int, b: int) -> int:
    return a + b


def sum_mod_bys(x: int, y: int) -> Option[int]:
    return ten_mod_by(x) \
        .fmap(sum) \
        .ap(ten_mod_by(y))

    return Option.pure(sum) \
        .ap(ten_mod_by(x)) \
        .ap(ten_mod_by(y))

# print(sum_mod_bys(4, 3))
# print(sum_mod_bys(4, 0))
# print(sum_mod_bys(0, 3))
# print(sum_mod_bys(0, 0))

def seven_mod_by(n: int) -> Option[int]:
    if n == 0:
        return Nothing()
    
    return Some(7 % n)


def three_mod_by(n: int) -> Option[int]:
    if n == 0:
        return Nothing()
    
    return Some(3 % n)


# def mod_bys(n: int) -> Option[int]:
#     return ten_mod_by(n) \
#         .flatmap(seven_mod_by) \
#         .flatmap(three_mod_by)

from funclift.fp.monad_runner import run_monads

def mod_bys(n: int):
    r10 = yield ten_mod_by(n)
    r7 = yield seven_mod_by(r10)
    return three_mod_by(r7)

monads = mod_bys(10)
result = run_monads(monads)
print(result)

# print(mod_bys(18))
# print(mod_bys(10))
# print(mod_bys(8))
# print(mod_bys(7))
# print(mod_bys(4))
# print(mod_bys(2))
# print(mod_bys(0))