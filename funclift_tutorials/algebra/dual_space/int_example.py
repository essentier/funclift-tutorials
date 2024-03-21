from dual_spaces import *

@dataclass
class IntD2:
    v1: int
    v2: int


def f(d2: IntD2) -> int:
    return d2.v1

# Unlike with Z3, here with int, we have infinite linear maps: int -> int
# We will just sample few of them
def d1s0(i: int) -> int:
    return i * 2

def d1s1(i: int) -> int:
    return i * 3

d1s_all = [d1s0, d1s1]

def d2s0(d2: IntD2) -> int:
    return d2.v1 * 2 + d2.v2

def d2s1(d2: IntD2) -> int:
    return d2.v1 + d2.v2 * 3 

d2s_all = [d2s0, d2s1]

def assert_equal_fss(fss1, fss2):
    for d1s in d1s_all:
        assert fss1(d1s) == fss2(d1s)
        print(f'fss(d1s) = {fss1(d1s)}')


if __name__ == '__main__':
    d2 = IntD2(2, 5)
    vss = ita(d2)

    vs = VS(d2s1)
    print(vss(vs))  # d2s1(d2)

    # fs0 = fs_all[0]
    # print(fs0)
    # print(x)
    # print(fs0(zd2))

    # zd2 = Z3D2(Z3.z1, Z3.z1)
    # fss0_a = ita(f(zd2))
    # fss0_b = ita(zd2).fmap(f)
    # assert_equal_fss(fss0_a, fss0_b)

    # for a1 in (Z3):
    #     for a2 in (Z3):
    #         zd2 = Z3D2(a1, a2)
    #         fss0_a = ita(f(zd2))
    #         fss0_b = ita(zd2).fmap(f)
    #         assert_equal_fss(fss0_a, fss0_b)
