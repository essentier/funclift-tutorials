# What if x can be None like this:


def add_5(x: int | None) -> int | None:
    if x is None:
        return None
    else:
        return x + 5


print(add_5(2))
print(add_5(None))
