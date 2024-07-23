# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return 41.21


class B:
    def __init__(self):
        pass

    def func(self):
        return (32, 72, 78)


class C(A, B):
    pass


c = C()
d = c.func()
