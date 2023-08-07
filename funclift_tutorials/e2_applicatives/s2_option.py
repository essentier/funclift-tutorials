# What if x or y can be None like this:


def add(x: int | None, y: int | None) -> int | None:
    if x is None or y is None:
        return None

    return x + y


print(add(5, 2))
print(add(5, None))
print(add(None, 2))
