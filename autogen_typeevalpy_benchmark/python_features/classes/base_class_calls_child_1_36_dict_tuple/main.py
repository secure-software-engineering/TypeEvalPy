# The base class calls a function defined by the child class.
class A:
    def func(self):
        return self.child()


class B(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return {'adxxy': 29, 'sooye': 57, 'tplwl': 21}


class C(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return (3, 26, 83)


b = B()
d = b.func()

c = C()
e = c.func()
