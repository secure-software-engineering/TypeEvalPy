# The base class calls a function defined by the child class.
class A:
    def func(self):
        return self.child()


class B(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return 7.53


class C(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return {'hyjtd': 20, 'ajlyp': 5, 'ixmjl': 13}


b = B()
d = b.func()

c = C()
e = c.func()
