# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 19.85


class B:
    def func(self):
        return 'gmpex'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [92, 5, 96]


c = C()
d = c.func()
