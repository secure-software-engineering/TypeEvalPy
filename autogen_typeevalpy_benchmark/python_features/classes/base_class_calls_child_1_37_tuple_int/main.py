# The base class calls a function defined by the child class.
class A:
    def func(self):
        return self.child()


class B(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return (31, 60, 5)


class C(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return 95


b = B()
d = b.func()

c = C()
e = c.func()
