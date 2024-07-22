# The base class calls a function defined by the child class.
class A:
    def func(self):
        return self.child()


class B(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return [94, 85, 72]


class C(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return {'vhmts': 11, 'urhig': 85, 'wnjkv': 12}


b = B()
d = b.func()

c = C()
e = c.func()
