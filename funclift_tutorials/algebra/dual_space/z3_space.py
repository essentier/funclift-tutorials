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


# generate fi
def generate_z3star_linear_maps():
    def make_z3star_linear_map(z):
        def f(x: Z3) -> Z3:
            return x * z   # need to define * on Z3
        return f

    fi = []
    for z in (Z3):
        fi.append(make_z3star_linear_map(z))
    return fi

def make_z3d2star_linear_map(a1: Z3, a2: Z3):
    def f(v: Z3D2) -> Z3:
        return a1 * v.v1 + a2 * v.v2   # need to define + on Z3
    return f
