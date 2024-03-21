# Zippers and Comonads in Haskell
# https://www.kuniga.me/blog/2013/10/01/zippers-and-comonads-in-haskell.html

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar
import logging

log = logging.getLogger(__name__)

A = TypeVar("A")
B = TypeVar("B")

@dataclass
class Universe(Generic[A]):
    left: [A]
    current: A
    right: [A]

    def go_right(self) -> Universe[A]:
        if len(self.right) == 0:
            return self
        
        return Universe([self.current] + self.left, self.right[0], self.right[1:])
    
    def go_left(self) -> Universe[A]:
        if len(self.left) == 0:
            return self

        return Universe(self.left[1:], self.left[0], [self.current] + self.right)
    
    def fmap(self, f: Callable[[A], B]) -> Universe[B]:
        return Universe(list(map(f, self.left)), f(self.current), list(map(f, self.right)))
    
    def extract(self) -> A:
        return self.current
    
    def duplicate(self) -> Universe[Universe[A]]:
        leftus = []
        x = self
        for _ in self.left:
            x = x.go_left()
            leftus = [x] + leftus

        rightus = []
        x = self
        for _ in self.right:
            x = x.go_right()
            rightus.append(x)

        return Universe(leftus, self, rightus)
    
    def extend(self, f: Callable[[Universe[A]], B]) -> Universe[B]:
        return self.duplicate().fmap(f)
    

    def shift(self, n: int) -> Universe[A]:
        x = self
        if n < 0:
            for _ in range(-n):
                x = x.go_left()
        else:
            for _ in range(n):
                x = x.go_right()
        return x

    def sample(self, n):
        samples = []
        x = self
        for _ in range(n):
            x = x.go_left()
            samples = [x.current] + samples
        
        samples.append(self.current)
        x = self
        for _ in range(n):
            x = x.go_right()
            samples.append(x.current)
        
        return samples
    
    def to_str(self, f) -> str:
        values = self.sample(40)
        return ''.join(map(f, values))
        

def rule(universe: Universe[bool]) -> bool:
    l = universe.left[0] if len(universe.left) > 0 else True
    r = universe.right[0] if len(universe.right) > 0 else True
    return not (l and universe.current and not r or (l == universe.current))

def bool_to_str(b: bool) -> str:
    return '#' if b else ' '


u1 = Universe([False] * 60, True, [False] * 60)
print(u1.to_str(bool_to_str))

for _ in range(5):
    u1 = u1.extend(rule)
    print(u1.to_str(bool_to_str))
