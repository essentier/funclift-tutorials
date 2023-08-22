
def foo(b: bool) -> int:
    return (-2 if b else 3)

def bar(n: int) -> str:
    return 'h' * abs(n)

def foo_then_bar(b: bool) -> str:
    '''
    Composing pure functions is straightforward.
    '''
    return bar(foo(b))

result = foo_then_bar(True)
print(result)
