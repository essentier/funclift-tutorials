# https://www.haskellforall.com/2013/02/you-could-have-invented-comonads.html

from __future__ import annotations

'''
Builder pattern

implement the objected-oriented builder design pattern
let's say that we have a Config value we want to build that just stores a list of program Options
'''

from dataclasses import dataclass
from typing import Any, Callable, Generic, TypeVar
import logging

log = logging.getLogger(__name__)

A = TypeVar("A")
B = TypeVar("B")

Option = str

@dataclass
class Config:
    options: [Option]


@dataclass
class Builder(Generic[A]):
    builder: Callable[[[Option]], A]

    def extract(self) -> A:
        return self.builder([])

    def extend(self: Builder[A], setter: Callable[[Builder[A]], B]) -> Builder[B]:
        def f(options2: [Option]) -> B:
            return setter(Builder(lambda options1: self.builder(options1 + options2)))

        return Builder(f)
    
    def build(self, options: [Option]) -> A:
        return self.builder(options)


def default_config_builder(options: [Option]) -> Config:
    return Config(['-Wall'] + options)


def profile(builder: Builder[Config]) -> Config:
    return builder.build(['-prof', '-auto-all'])

def go_faster(builder: Builder[Config]) -> Config:
    return builder.build(['-O2'])

# profile_config = profile(default_config_builder)
# print(profile_config)

b = Builder(default_config_builder)
b1 = b.extend(go_faster).extend(profile)
config1 = b1.extract()
print(config1)
