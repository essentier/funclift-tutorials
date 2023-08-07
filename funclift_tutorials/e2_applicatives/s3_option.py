from funclift.types.option import Option, Some, Nothing
from funclift.fp.curry import curry

# use the Option applicative


@curry
def add(x: int, y: int) -> int:
    return x + y


value1: Option[int] = Some(5)
value2: Option[int] = Some(2)
print(Option.pure(add).ap(value1).ap(value2))
print(value1.fmap(add).ap(value2))

nothing: Option[int] = Nothing()
print(Option.pure(add).ap(nothing).ap(value2))
print(value1.fmap(add).ap(nothing))
