from funclift.types.option import Option, Some, Nothing

# use the Option functor


def add_5(x: int) -> Option[int]:
    if x > 7:
        return Nothing()

    return Some(x + 5)


value1: Option[int] = Some(2)
print(value1.flatmap(add_5))

value2: Option[int] = Nothing()
print(value2.flatmap(add_5))
