# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'qqmcr'


class B:
    def func(self):
        return 76


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'obema': 19, 'lvppd': 56, 'dfvyo': 47}


c = C()
d = c.func()
