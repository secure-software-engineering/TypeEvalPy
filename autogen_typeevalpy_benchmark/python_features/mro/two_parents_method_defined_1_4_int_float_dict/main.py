# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 4


class B:
    def func(self):
        return 57.13


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'whqzj': 87, 'xvgpm': 63, 'lzwgi': 100}


c = C()
d = c.func()
