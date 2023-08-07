# Why do we do it?
# Besides abstract common pattern. Code refactoring, one big reason is
# referential transparency (e.g. IO, reader, writer, state functors/monads)
# Let's look at an example

# performs side effect.
print('PyCon Latam')

# solution
from funclift.funclift.types.io import IO
 
def print2(text: str) -> IO[None]:
    return IO(lambda: print(text))

io = print2('PyCon Latam')

# do things that are side-effect free.
# only trigger the side effect here. 
io.unsafe_run()


# referential transparency


# do-notation