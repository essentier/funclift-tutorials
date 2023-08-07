# sometimes, functor is not enough
# for example, we want to add two numbers

def add(a: int, b: int) -> int:
    return a + b

print(add(5, 2))

# what if a and/or b can be None

def add(a: int | None, b: int | None) -> int | None:
    if a == None:
        return None
    
    if b == None:
        return None
    
    return a + b

value1: int | None = 2 # or None
value2: int | None = 5 # or None
print(add(value1, value2))

# use the Option functor?
# But fmap only takes functions like int -> int, not
# int -> int -> int
# We need to use Applicative.
@curry
def add(a: int, b: int) -> int:
    return a + b

some_value: Option[int] = Some(2) # or Nothing()
print(some_value.fmap(add_5))
