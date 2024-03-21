from dataclasses import dataclass
from enum import Enum

class Z3(Enum):
    z0 = 0
    z1 = 1
    z2 = 2

    def __mul__(self, other): 
        return Z3((self.value * other.value) % 3)

    def __add__(self, other): 
        return Z3((self.value + other.value) % 3)


# Z3D2 is a two-dimentional vector space over Z3. Its vectors are (a, b) where a and b are Z3 instances.
@dataclass
class Z3D2:
    v1: Z3
    v2: Z3


def make_z3d2star_linear_map(a1: Z3, a2: Z3):
    def f(v: Z3D2) -> Z3:
        return a1 * v.v1 + a2 * v.v2   # need to define + on Z3
    return f


# Z3D2Star (Z3D2*) is the dual space of Z3D2. Its vectors are functions f: Z3D2 -> Z3.
class Z3D2Star:
    def __init__(self, a1: Z3, a2: Z3) -> None:
        self.f = make_z3d2star_linear_map(a1, a2)

    def __call__(self, z: Z3D2) -> Z3:
        return self.f(z)

if __name__ == '__main__':
    print(f'1 + 2*2 = {Z3D2Star(Z3.z1, Z3.z2)(Z3D2(Z3.z1, Z3.z2))}')
    # print(f'f1(1) = {Z3D2Star(Z3.z1)(Z3.z1)}')
    # print(f'f1(2) = {Z3D2Star(Z3.z1)(Z3.z2)}')
