

def foo():
    yield 1
    yield 2
    yield 3


import itertools

result = itertools.chain([5], foo())
print(list(result))