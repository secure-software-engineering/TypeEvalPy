# The base class calls a function defined by the child class.
class A:
    def func(self):
        return self.child()


class B(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return True


class C(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return {'rofqr': 55, 'bcret': 50, 'muayq': 51}


b = B()
d = b.func()

c = C()
e = c.func()
