# https://www.haskellforall.com/2013/02/you-could-have-invented-comonads.html

# The iterator pattern

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar, Iterator
import logging
import itertools as it

log = logging.getLogger(__name__)

A = TypeVar("A")
B = TypeVar("B")


@dataclass
class MyIterator(Generic[A]):
    empty: A
    items: list[A]

    # def __init__(self, empty: A, items: Iterator[A]):
    #     self.empty = empty
    #     self.items = it.chain(items, it.repeat(empty))

    def extract(self) -> A:
        if len(self.items) == 0:
            return self.empty
        
        return self.items[0]

    def extend(self: MyIterator[A], it: Callable[[MyIterator[A]], A]) -> MyIterator[A]:
        if len(self.items) == 0:
            return self
    
        new_items = [it(self)] + MyIterator(self.empty, self.items[1:]).extend(it).items
        return MyIterator(self.empty, new_items)


def next(it: MyIterator[A]) -> A:
    if len(it.items) < 2:
        return it.empty
    
    return it.items[1]

def next2(it: MyIterator[A]) -> A:
    if len(it.items) < 3:
        return it.empty
    
    return it.items[2]


example_history = MyIterator('', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
print(next(example_history))

example_history2 = example_history.extend(next)
print(next(example_history2))

example_history3 = example_history.extend(next2).extend(next2)
print(example_history3.extract())
print(example_history3)
