# This tests the simple rule of MRO: Most specific first.

# MRO appends the superclasses of the parents in the inheritance chain. So the inheritance chain should look like this: D -> B -> A -> object -> C -> A -> object
# However, since A and object appear later in the chain, that means that more specific versions exist, so the correct inheritance chain is: D -> B -> C -> A -> object


class A:
    def __init__(self):
        pass

    def func(self):
        return 99.2


class B(A):
    pass


class C(A):
    def func(self):
        return 42


class D(B, C):
    pass


d = D()
e = d.func()
