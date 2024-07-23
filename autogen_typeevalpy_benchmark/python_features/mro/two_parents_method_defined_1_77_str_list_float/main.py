# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'uqwgi'


class B:
    def func(self):
        return [88, 71, 72]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 43.23


c = C()
d = c.func()
