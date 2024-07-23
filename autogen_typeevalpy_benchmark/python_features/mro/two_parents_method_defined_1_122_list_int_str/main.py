# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [54, 79, 28]


class B:
    def func(self):
        return 48


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'inhis'


c = C()
d = c.func()
