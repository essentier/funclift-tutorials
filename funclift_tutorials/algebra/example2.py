from enum import Enum

class Z3(Enum):
    z0 = 0
    z1 = 1
    z2 = 2

    def __mul__(self, other): 
        return Z3((self.value * other.value) % 3)


# def f0(z3: Z3) -> Z3:
#     return Z3.z0

# def f1(z3: Z3) -> Z3:
#     return z3

# def f2(z3: Z3) -> Z3:
#     match z3:
#         case Z3.z0:
#             return Z3.z0
#         case Z3.z1:
#             return Z3.z2
#         case Z3.z2:
#             return Z3.z1

# print(f'f2(0) = {f2(Z3.z0)}')
# print(f'f2(1) = {f2(Z3.z1)}')
# print(f'f2(2) = {f2(Z3.z2)}')


# generate fi
def generate_z3star_linear_maps():
    def make_z3star_linear_map(z):
        def f(x: Z3) -> Z3:
            return x * z   # need to define * on Z3
        return f

    fi = []
    for z in (Z3):
        # https://stackoverflow.com/questions/3431676/creating-functions-or-lambdas-in-a-loop-or-comprehension
        # This is a problem with late binding -- each function looks up i as late as possible 
        # (thus, when called after the end of the loop, z will be set to Z3.z2).
        # def f(x: Z3, z=z) -> Z3:
        #     # print(f'multiply {z} and {x}')
        #     return x * z   # need to define * on Z3
        
        fi.append(make_z3star_linear_map(z))
    return fi

[f0, f1, f2] = generate_z3star_linear_maps()


# Z3Star (Z3*) is the dual space of Z3. Its vectors are functions f: Z3 -> Z3.
class Z3Star:
    fs = generate_z3star_linear_maps()

    def __init__(self, z: Z3) -> None:
        self.f = Z3Star.fs[z.value]

    def __call__(self, z: Z3) -> Z3:
        return self.f(z)

# print(f'f1(0) = {Z3Star(Z3.z1)(Z3.z0)}')
# print(f'f1(1) = {Z3Star(Z3.z1)(Z3.z1)}')
# print(f'f1(2) = {Z3Star(Z3.z1)(Z3.z2)}')

# Z3Star2 (Z3**) is the dual space of Z3*. Its vectors are functions f: Z3Star -> Z3.
class Z3Star2:
    def __init__(self, z: Z3) -> None:
        self.z = z

    def __call__(self, f: Z3Star) -> Z3:
        return f(self.z)

if __name__ == '__main__':
    print(f'f1(0) = {f1(Z3.z0)}')
    print(f'f1(1) = {f1(Z3.z1)}')
    print(f'f1(2) = {f1(Z3.z2)}')

    # print(f'f2(0) = {f2(Z3.z0)}')
    # print(f'f2(1) = {f2(Z3.z1)}')
    # print(f'f2(2) = {f2(Z3.z2)}')

    z2_hat = Z3Star2(Z3.z2)
    print(f'z2_hat(f0) = {z2_hat(Z3Star(Z3.z0))}')
    print(f'z2_hat(f1) = {z2_hat(Z3Star(Z3.z1))}')
    print(f'z2_hat(f2) = {z2_hat(Z3Star(Z3.z2))}')