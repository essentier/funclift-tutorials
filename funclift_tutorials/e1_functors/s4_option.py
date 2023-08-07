# So what is a functor? 
# effect (not necessarily side effect)
# something that performs an effect when you map it over a function
# lifts a function
# wraps an object


def ws(x: int) -> str:
    return 'w' * x


some_value: Option[int] = Some(2)  # or Nothing()
print(some_value.fmap(ws))
