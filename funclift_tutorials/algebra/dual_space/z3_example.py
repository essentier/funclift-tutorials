# organize the code
# fields: int, Z3, Z5
# vector space: polynomials, matrices
# inner product, transpose


from z3_space import Z3, Z3D2, generate_z3star_linear_maps, make_z3d2star_linear_map
from dual_spaces import *

def f(zd2: Z3D2) -> Z3:
    return zd2.v1

# def generate_z3d2star_linear_maps():

#     fi = []
#     for a1 in (Z3):
#         for a2 in (Z3):
#             fi.append(VS(make_z3d2star_linear_map(a1, a2)))
#     return fi

# fs_all = generate_z3d2star_linear_maps()

fs_all = generate_z3star_linear_maps()

def assert_equal_fss(fss1, fss2):
    for fs in fs_all:
        assert fss1(fs) == fss2(fs)
        print(f'fss(fs) = {fss1(fs)}')


if __name__ == '__main__':
    zd2 = Z3D2(Z3.z1, Z3.z0)
    vss = ita(zd2)

    vs = VS(make_z3d2star_linear_map(Z3.z2, Z3.z1))
    print(vss(vs))

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
