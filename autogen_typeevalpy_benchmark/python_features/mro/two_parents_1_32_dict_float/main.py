# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return {'jupcz': 43, 'vrkjt': 9, 'slkzp': 13}


class B:
    def __init__(self):
        pass

    def func(self):
        return 2.31


class C(A, B):
    pass


c = C()
d = c.func()
