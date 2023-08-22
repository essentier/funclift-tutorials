import time
import asyncio
from funclift.types.aio import AIO
from funclift.fp.monad_runner import run_monads


async def cook(meat):
    print(f'start cooking {meat}')
    await asyncio.sleep(5)
    print(f'finish cooking {meat}')
    return f'cooked {meat}'

async def prepare_cheese(cheese_type):
    print('start preparing cheese')
    await asyncio.sleep(2)
    print('finish preparing cheese')
    return cheese_type

async def melt(thing):
    print(f'start melting {thing}')
    await asyncio.sleep(2)
    print(f'finish melting {thing}')
    return f'melted {thing}'


async def fold_into_tortilla(*args):
    print('start folding filling into tortilla')
    await asyncio.sleep(1)
    print('finish folding filling into tortilla')
    return f'quesadilla made from {args}'

async def cook_and_slice(quesadilla):
    print('start cooking and slicing')
    await asyncio.sleep(1)
    print('finish cooking and slicing')
    return f'cooked and sliced {quesadilla}'

async def make_cheese(cheese_type):
    cheese = await prepare_cheese(cheese_type)
    melted = await melt(cheese)
    return melted

async def make_quesadilla():
    print(f"started at {time.strftime('%X')}")
    tasks = []
    async with asyncio.TaskGroup() as tg:
        task = tg.create_task(cook('ground beef'))
        tasks.append(task)
        task = tg.create_task(make_cheese('cheddar cheese'))
        tasks.append(task)

    fillings = [task.result() for task in tasks]
    quesadilla = await fold_into_tortilla(*fillings)
    result = await cook_and_slice(quesadilla)
    print(f"finished at {time.strftime('%X')}")
    print('Enjoy:', result)

# asyncio.run(make_quesadilla())

# Another way
def create_quesadilla_aio():
    return AIO.pure(prepare_cheese('cheddar cheese')) \
        .then(melt) \
        .par(cook('ground beef')) \
        .then(fold_into_tortilla) \
        .then(cook_and_slice)

async def quesadilla_aio_example():
    quesadilla_aio = create_quesadilla_aio()
    print(f"started at {time.strftime('%X')}")
    result = await quesadilla_aio.unsafe_run()
    print(f"finished at {time.strftime('%X')}")
    print('Enjoy:', result)

asyncio.run(quesadilla_aio_example())


# Another way
def create_program_monads():
    cheese_aio = AIO.pure(prepare_cheese('cheddar cheese')) \
        .then(melt)
    
    meat_aio = AIO.pure(cook('ground beef'))
    filling_aio = AIO.group(meat_aio, cheese_aio) 
    fillings = yield filling_aio
    quesadilla = yield AIO.pure(fold_into_tortilla(*fillings))
    result = yield cook_and_slice(quesadilla)
    return AIO.succeed(result)

async def quesadilla_do_notation_example():
    monads = create_program_monads()
    program = run_monads(monads)

    print(f"started at {time.strftime('%X')}")
    task = program.unsafe_run()
    result = await task
    print(f"finished at {time.strftime('%X')}")
    print('Enjoy:', result)

# asyncio.run(quesadilla_do_notation_example())