# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'apupw'


class B:
    def func(self):
        return 11.21


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [6, 1, 22]


c = C()
d = c.func()
