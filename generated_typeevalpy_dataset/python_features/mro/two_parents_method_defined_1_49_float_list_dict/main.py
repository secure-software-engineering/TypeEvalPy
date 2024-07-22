# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 57.15


class B:
    def func(self):
        return [15, 31, 33]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'vdhjt': 18, 'rwahi': 14, 'zrgyg': 89}


c = C()
d = c.func()
