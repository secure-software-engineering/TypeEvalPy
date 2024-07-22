# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return {'ivzhh': 50, 'zaveb': 21, 'esvki': 19}


class B:
    def __init__(self):
        pass

    def func(self):
        return 3


class C(A, B):
    pass


c = C()
d = c.func()
