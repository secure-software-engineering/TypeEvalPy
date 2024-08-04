# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'ilghb'


class B:
    def func(self):
        return {'znodo': 13, 'egrik': 64, 'lgtzj': 62}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 62.15


c = C()
d = c.func()
