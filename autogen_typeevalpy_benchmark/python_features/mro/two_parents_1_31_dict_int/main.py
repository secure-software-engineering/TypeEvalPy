# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return {'brpiw': 2, 'dvlak': 91, 'lhnnz': 81}


class B:
    def __init__(self):
        pass

    def func(self):
        return 9


class C(A, B):
    pass


c = C()
d = c.func()
