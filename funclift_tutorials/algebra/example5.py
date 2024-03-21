from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Generic, TypeVar
from functools import reduce

V = TypeVar('V')
W = TypeVar('W')
F = TypeVar('F')


# https://www.geeksforgeeks.org/function-composition-in-python/
# def composite_function(*func):
      
#     def compose(f, g):
#         return lambda x : f(g(x))
              
#     return reduce(compose, func, lambda x : x)


@dataclass
class VS(Generic[W, F]):
    ws: Callable[[W], F] # func: W -> F

    # Given f, we can lift it to f*
    def contrafmap(self, f: Callable[[V], W]) -> VS[V, F]:
        def _f(v: V) -> F:
            return self.ws(f(v))
        return VS(_f)

    def __call__(self, v: V) -> F:
        return self.ws(v)


# implement the functor (-)**
@dataclass
class VSS(Generic[V, F]):
    vss: Callable[[VS[V, F]], F]  # func: VS -> F

    # Given f, we can lift it to f**
    def fmap(self, f: Callable[[V], W]) -> VSS[W]:
        # # fs: WS -> VS
        # def fs(ws: VS[W, F]) -> VS[V, F]:
        #     return VS(composite_function(ws, f))
        # return VSS(composite_function(self, fs))

        def _f(ws: VS[W, F]) -> F:
            return self.vss(lambda v: ws(f(v)))
            # return self.vss(ws(lambda v: f(v)))
            # return composite_function(ws, f)
        return VSS(_f)

    
    def __call__(self, vs: VS[V, F]) -> F:
        return self.vss(vs)


# implement the natural transformation ita: Id -> (-)**
def ita(v: V) -> VSS[V, F]:
    def vss(vs: VS[V, F]) -> F:
        return vs(v)
    return VSS(vss)

