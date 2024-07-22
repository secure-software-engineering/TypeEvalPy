# The base class calls a function defined by the child class.
class A:
    def func(self):
        return self.child()


class B(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return (8, 94, 56)


class C(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return {'xddfc': 59, 'cfvww': 80, 'gxalq': 81}


b = B()
d = b.func()

c = C()
e = c.func()
