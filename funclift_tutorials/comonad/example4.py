# https://chshersh.com/posts/2019-03-25-comonadic-builders

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar, Type
from funclift.monoid import Monoid, get_mempty

import logging

log = logging.getLogger(__name__)

A = TypeVar("A", contravariant=True)
B = TypeVar("B")
F = TypeVar("F")
M = TypeVar('M', bound=Monoid | str)

# Identity comonad
@dataclass
class Identity(Generic[A]):
    a: A

    def extract(self) -> A:
        return self.a
    
    def duplicate(self) -> Identity[Identity[A]]:
        return Identity(self)
    
    def extend(self: Identity[A], f: Callable[[Identity[A]], B]) -> Identity[B]:
        return Identity(f(self))
    
# Arrow comonad
@dataclass
class Arrow(Generic[M, A]):
    # mcls: type # type of M
    mcls: Type[M]
    builder: Callable[[M], A]

    def fmap(self: Arrow[M, A], f: Callable[[A], B]) -> Arrow[M, B]:
        def _f(m: M) -> B:
            return f(self.builder(m))
        
        return Arrow(self.mcls, _f)


    def extract(self) -> A:
        empty: M = get_mempty(self.mcls)
        return self.builder(empty)


    def duplicate(self) -> Arrow[M, Arrow[M, A]]:
        # def f(m1: M, m2: M) -> A:
        #     return self.builder(m1 + m2)
        def f(m1: M) -> Arrow[M, A]:
            def g(m2: M) -> A:
                return self.builder(m1 + m2)
            return Arrow(self.mcls, g)
        
        return Arrow(self.mcls, f)
    
    def extend(self: Arrow[M, A], f: Callable[[Arrow[M, A]], B]) -> Arrow[M, B]:
        return self.duplicate().fmap(f)
    
    def build(self: Arrow[M, A], m: M) -> A:
        return self.builder(m)


def foo(n: int) -> str:
    return 'hi from foo' * n

def bar(arrow: Arrow[int, str]) -> str:
    return arrow.build(2)

def baz(arrow: Arrow[int, str]) -> str:
    return arrow.build(3)

a1 = Arrow(int, foo)
a2 = a1.extend(bar).extend(baz)
print(a2.extract())
