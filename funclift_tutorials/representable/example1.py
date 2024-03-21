

# https://jozefg.bitbucket.io/posts/2013-10-21-representable-functors.html

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar, Type
from funclift.monoid import Monoid
from funclift.functor import Functor

import logging

log = logging.getLogger(__name__)

Obj = TypeVar("Obj")
A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
F = TypeVar("F")
G = TypeVar("G")
M = TypeVar('M', bound=Monoid | str)

# Hom Functor
@dataclass
class Hom(Generic[Obj, A]):
    homf: Callable[[Obj], A]

    def fmap(self, f: Callable[[A], B]) -> Hom[Obj, B]:
        def h(obj: Obj) -> B:
            return f(self.homf(obj))
        
        return Hom(h)
    
    def __call__(self, obj: Obj) -> A:
        return self.homf(obj)


# Representable
class Representable:

    @staticmethod
    def to_hom(fa: Functor[F, A], cls: Type[Obj]) -> Hom[Obj, A]:
        ...
    
    @staticmethod
    def to_functor(hom: Hom[Obj, A]) -> Functor[F, A]:
        ...

def lookup(fa: Functor[F, A], obj: Obj) -> A:
    return Representable.to_hom(fa, type(obj))(obj)

class Unit:
    ...

# Identity is representable
@dataclass
class Identity(Generic[A]):
    a: A

    def to_hom(self) -> Hom[Unit, A]:
        def h(_: Unit) -> A:
            return self.a
        
        return Hom(h)
    
    @staticmethod
    def to_functor(hom: Hom[Unit, A]) -> Identity[A]:
        return Identity(hom(Unit()))


# Prod is representable
# use bool as the index object type.
# True for right, False for left
@dataclass
class Prod(Generic[A]):
    left: A
    right: A

    def to_hom(self) -> Hom[bool, A]:
        def h(b: bool) -> A:
            return self.right if b else self.left
        
        return Hom(h)
    
    @staticmethod
    def to_functor(hom: Hom[bool, A]) -> Prod[A]:
        return Prod(hom(False), hom(True))

'''
https://chrispenner.ca/posts/representable-discrimination

We've got a Representable Functor r; 
If we have a Rep r for some 'a'
 we know which slot to put it into in an r a. We can get a Rep r for every a by using a function a -> Rep r. Now we want to embed the a into an r a using the Rep r, the tool we have for this is tabulate, in order to know which index is which and put it into the right slot we'll need to require Eq (Rep r). We know which slot our one element goes to, but we need something to put into all the other slots. If a were a Monoid we could use mempty for the other slots; then if we map that function over every element in an input list we could build something like this:

'''

# Forever is representable
# use int as the index object type.
@dataclass
class Forever(Generic[A]):
    items: [A]

    def to_hom(self) -> Hom[int, A]:
        def h(i: int) -> A:
            return self.items[i] # index out-of-bound
        
        return Hom(h)
    
    @staticmethod
    def to_functor(hom: Hom[int, A]) -> Forever[A]:
        return Forever([hom(0), hom(1), hom(2)]) # ???
