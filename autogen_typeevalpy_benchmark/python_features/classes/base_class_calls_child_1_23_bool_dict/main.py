# The base class calls a function defined by the child class.
class A:
    def func(self):
        return self.child()


class B(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return False


class C(A):
    def __init__(self):
        self.child = self.func2

    def func2(self):
        return {'lpbhc': 35, 'uyzgf': 54, 'eupbj': 29}


b = B()
d = b.func()

c = C()
e = c.func()
