# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'fsagm': 53, 'imzpd': 12, 'lmctu': 14}


class B:
    def func(self):
        return 5.69


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [5, 8, 94]


c = C()
d = c.func()
