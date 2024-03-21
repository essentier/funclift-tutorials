

from example2 import generate_z3star_linear_maps
from example3 import Z3
from example5 import *

def f(z: Z3) -> Z3:
    match z:
        case Z3.z0:
            return Z3.z0
        case Z3.z1:
            return Z3.z2
        case Z3.z2:
            return Z3.z1

[fs0, fs1, fs2] = generate_z3star_linear_maps()

def assert_equal_fss(fss1, fss2):
    assert fss1(fs0) == fss2(fs0)
    assert fss1(fs1) == fss2(fs1)
    assert fss1(fs2) == fss2(fs2)
    print(f'fss(fs0) = {fss1(fs0)}')
    print(f'fss(fs1) = {fss1(fs1)}')
    print(f'fss(fs2) = {fss1(fs2)}')

if __name__ == '__main__':
    fss0_a = ita(f(Z3.z0))
    fss0_b = ita(Z3.z0).fmap(f)
    assert_equal_fss(fss0_a, fss0_b)

    fss1_a = ita(f(Z3.z1))
    fss1_b = ita(Z3.z1).fmap(f)
    assert_equal_fss(fss1_a, fss1_b)

    fss2_a = ita(f(Z3.z2))
    fss2_b = ita(Z3.z2).fmap(f)
    assert_equal_fss(fss2_a, fss2_b)
