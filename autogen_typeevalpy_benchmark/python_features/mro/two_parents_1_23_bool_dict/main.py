# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return True


class B:
    def __init__(self):
        pass

    def func(self):
        return {'rkrrj': 50, 'wgaaq': 75, 'ssmrq': 77}


class C(A, B):
    pass


c = C()
d = c.func()
