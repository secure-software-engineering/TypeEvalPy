# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return [83, 12, 2]


class B:
    def __init__(self):
        pass

    def func(self):
        return {'hpdrr': 31, 'adonc': 7, 'cxdmo': 50}


class C(A, B):
    pass


c = C()
d = c.func()
