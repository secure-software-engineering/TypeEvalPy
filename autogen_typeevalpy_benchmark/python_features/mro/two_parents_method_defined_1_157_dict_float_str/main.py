# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'dcxym': 93, 'hhxor': 88, 'ufhbd': 60}


class B:
    def func(self):
        return 73.09


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'dmgwt'


c = C()
d = c.func()
