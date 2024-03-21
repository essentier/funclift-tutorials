from dataclasses import dataclass
from typing import Tuple

from funclift.types.option import Option, Some, Nothing
from funclift.types.either import Either, Left



@dataclass
class InnerData:
    bar: str
    foo: Tuple[str, Either[int, bool]]


type NestedData = Option[list[InnerData]]


def get_nested_int(index: int, nested_data: NestedData) -> Option[int]:
    match nested_data:
        case Nothing():
            return Nothing()
        case Some(arr):
            eitherInt = arr[index].foo[1]
            match eitherInt:
                case Left(i):
                    return Some(i)
                case _:
                    return Nothing()
                
    


def run_example():
    print('run example')
    nested_data = Some([InnerData('value10', ('value11', Left(1))), InnerData('value20', ('value21', Left(2)))])
    result = get_nested_int(1, nested_data)
    print(result)


if __name__ == '__main__':
    run_example()