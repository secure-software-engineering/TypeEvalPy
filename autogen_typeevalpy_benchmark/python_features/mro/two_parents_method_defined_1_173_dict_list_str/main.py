# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'rnumn': 40, 'ayaqp': 99, 'unxou': 38}


class B:
    def func(self):
        return [21, 55, 72]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'dwspk'


c = C()
d = c.func()
