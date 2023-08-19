def ten_mod_by_v0(n: int) -> int:
    return 10 % n

# print(ten_mod_by_v0(4))

# ZeroDivisionError
# print(ten_mod_by_v0(0))

def ten_mod_by(n: int) -> int | None:
    if n == 0:
        return None
    
    return 10 % n

# print(ten_mod_by(4))
# print(ten_mod_by(1))
# print(ten_mod_by(0))

def remainder_in_text(r: int) -> str:
    return 'remainder is ' + str(r)


def ten_mod_by_in_text(x: int) -> str | None:
    r = ten_mod_by(x)
    if r:
        return remainder_in_text(r)
    else:
        return None

# print(ten_mod_by_in_text(4))
# print(ten_mod_by_in_text(0))

def sum(a: int, b: int) -> int:
    return a + b


def sum_mod_bys(x: int, y: int) -> int | None:
    rx = ten_mod_by(x)
    ry = ten_mod_by(y)
    if rx and ry:
        return sum(rx, ry)
    else:
        return None

# print(sum_mod_bys(4, 3))
# print(sum_mod_bys(4, 0))
# print(sum_mod_bys(0, 3))
# print(sum_mod_bys(0, 0))


def seven_mod_by(n: int) -> int | None:
    if n == 0:
        return None
    
    return 7 % n


def three_mod_by(n: int) -> int | None:
    if n == 0:
        return None
    
    return 3 % n

def mod_bys(n: int) -> int | None:
    r10 = ten_mod_by(n)
    if r10:
        r7 = seven_mod_by(r10)
        if r7:
            return three_mod_by(r7)
        else:
            return None
    else:
        return None

# print(mod_bys(18))
# print(mod_bys(10))
# print(mod_bys(8))
# print(mod_bys(7))
# print(mod_bys(4))
# print(mod_bys(2))
# print(mod_bys(0))