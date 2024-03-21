# https://www.works-hub.com/learn/representable-functors-by-example-6c5c0

class NatTx(Generic[A]):
    f: Functor[F, A]
    g: Functor[G, A]

def option_to_list(op: Option[A]) -> [A]:

