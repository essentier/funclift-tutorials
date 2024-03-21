# dual space and transpose of linear transformation

from dataclasses import dataclass

# Poly1 is a vector space. Its vectors are polynomials of degree at most 1.
class Poly1:
    def __init__(self, f) -> None:
        self.f = f

    # p(x) = 2x + 1
    def __call__(self, x: int) -> int:
        return self.f(x)
        

# R2 is a vector space. Its vectors are (a, b) where a and b are integers.
# Maybe it's more appropriate to call it Int2.
@dataclass
class R2:
    v1: int
    v2: int

# t is a linear transformation: Poly1 -> R2 
def t(p: Poly1) -> R2:
    return R2(p(0) - 2*p(1), p(0))

# Use t to transform polynomial p(x) = 1 + 2x to the vector (-5, 1) in R2.
result = t(Poly1(lambda x: 1 + 2*x))
print(result)

# R2Star (R2*) is the dual space of R2. Its vectors are functions f: R2 -> int.
class R2Star:
    def __init__(self, f) -> None:
        self.f = f

    # p(x) = 2x + 1
    def __call__(self, x: R2) -> int:
        return self.f(x)

# r2star_f is a vector in the dual space R2Star.
r2star_f = R2Star(lambda r2: r2.v1 - 2 * r2.v2)


# Poly1Star (Poly1*) is the dual space of Poly1. Its vectors are functions f: Poly1 -> int.
class Poly1Star:
    def __init__(self, f) -> None:
        self.f = f

    # p(x) = 2x + 1
    def __call__(self, p: Poly1) -> int:
        return self.f(p)


# tt is the transpose of t.
def tt(r2star: R2Star) -> Poly1Star:
    return Poly1Star(lambda p: r2star(t(p)))

poly1star_f = tt(r2star_f)
result = poly1star_f(Poly1(lambda x: 1 + 2*x))
print(result)