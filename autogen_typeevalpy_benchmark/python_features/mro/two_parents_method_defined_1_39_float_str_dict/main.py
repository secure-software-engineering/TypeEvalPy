# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 1.7


class B:
    def func(self):
        return 'sfqdg'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'mhmgj': 99, 'zqdmg': 82, 'apyjf': 24}


c = C()
d = c.func()
