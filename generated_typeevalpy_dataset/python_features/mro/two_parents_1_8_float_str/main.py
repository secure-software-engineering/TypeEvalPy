# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return 84.76


class B:
    def __init__(self):
        pass

    def func(self):
        return 'exgxd'


class C(A, B):
    pass


c = C()
d = c.func()
