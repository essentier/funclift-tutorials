# generate Z3
from enum import Enum

# class FFMeta(type):
#     def __new__(cls, name, bases, attrs):
#         uppercase_attrs = { key.upper(): value for key, value in attrs.items() if not key.startswith('__') }
#         return super().__new__(cls, name, bases, uppercase_attrs)

# class Foo(metaclass=FFMeta):
#     message = "hi"

# print(Foo.MESSAGE)

def make_zn(n: int) -> type:
    ns = {}
    for i in range(n):
        ns[f'z{i}'] = i
    
    cls = type(f'Z{n}', (), ns)

    def mul(self, other): 
        return cls((self.value * other.value) % n)

    def add(self, other): 
        return cls((self.value + other.value) % n)

    setattr(cls, "__mul__", mul)
    setattr(cls, "__add__", add)
    return cls

def make_zn_enum(n: int) -> type:
    ns = {}
    for i in range(n):
        ns[f'z{i}'] = i

    cls = Enum(f'Z{n}', ns)
    def mul(self, other): 
        return cls((self.value * other.value) % n)

    def add(self, other): 
        return cls((self.value + other.value) % n)

    setattr(cls, "__mul__", mul)
    setattr(cls, "__add__", add)
    return cls


if __name__ == '__main__':
    Z3 = make_zn_enum(3)
    # print(Z3.__dict__)

    print((Z3.z2 + Z3.z1 + Z3.z2)*Z3.z2)

