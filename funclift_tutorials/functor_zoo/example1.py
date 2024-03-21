from __future__ import annotations

from funclift.types.option import Option, Nothing, Some
from funclift.types.clist import CList
from funclift.types.either import Right, Either, Left
from funclift.types.compose import Compose

from typing import TypeVar
import logging

log = logging.getLogger(__name__)

A = TypeVar('A', covariant=True)


def get_head(nums: CList[A]) -> Option[A]:
   return Nothing() if len(nums.to_list()) == 0 else Some(nums.to_list()[0])

def is_even(n: int) -> bool:
   return n % 2 == 0

def add3(n: int) -> int:
   return n + 3

nums = CList([Some(1), Nothing(), Some(2)])
result = nums.fmap(Option.flift(is_even))
assert result == CList([Some(False), Nothing(), Some(True)])

composite = Compose(nums)
result = composite.fmap(add3).fmap(is_even)
print(f'composite result: {result}')
assert result == Compose(CList([Some(True), Nothing(), Some(False)]))

nums = CList([1, 2, 3, 4])
result1 = get_head(nums.fmap(is_even))
result2 = get_head(nums).fmap(is_even)
print(result1)
print(result2)

def add1(n: int) -> int:
    return n + 1

def negate(b: bool) -> bool:
    return not b 

v1: Either[bool, int] = Right(5)
v2 = v1.bimap(negate, add1)
assert v2 == Right(6)

v3: Either[bool, int] = Left(False)
v4 = v3.bimap(negate, add1)
assert v4 == Left(True)


# def ten_mod_by(n: int) -> str:
#    return 'zero' if n == 0 else 'value'

# print(ten_mod_by(4))
# print(ten_mod_by(0))
