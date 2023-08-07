from funclift.types.option import Option, Some, Nothing

# use the Option functor


def add_5(x: int) -> int:
    return x + 5


value1: Option[int] = Some(2)
print(value1.fmap(add_5))

value2: Option[int] = Nothing()
print(value2.fmap(add_5))
