# https://www.haskellforall.com/2013/02/you-could-have-invented-comonads.html

'''
Builder pattern

implement the objected-oriented builder design pattern
let's say that we have a Config value we want to build that just stores a list of program Options
'''

from dataclasses import dataclass
from typing import Callable, Generic, Protocol, TypeVar

Option = str

@dataclass
class Config:
    options: [Option]

'''
Let's say we don't want users to create Config instances directly or 
pattern match on Config. Instead, we want them to call this function 
to create config instances.
'''
def config_builder(options: [Option]) -> Config:
    return Config(options)

def default_config_builder(options: [Option]) -> Config:
    return Config(['-Wall'] + options)

Builder = Callable[[[Option]], Config]

def profile(builder: Builder) -> Config:
    return builder(['-prof', '-auto-all'])

def go_faster(builder: Builder) -> Config:
    return builder(['-O2'])

profile_config = profile(default_config_builder)
print(profile_config)

def extract(builder: Builder) -> Config:
    return builder([])

Builder = Callable[[[Option]], Config]

# def extend(setter: Callable[[Builder], Config]) -> Callable[[Builder], Builder]:
def extend(setter: Callable[[Builder], Config], builder: Builder) -> Builder:
    def f(options2: [Option]) -> Config:
        return setter(lambda options1: builder(options1 + options2))

    return f 

config1 = extract(extend(go_faster, default_config_builder))
print(config1)
