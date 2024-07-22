# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [64, 40, 99]


class B:
    def func(self):
        return 29


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'gmswj'


c = C()
d = c.func()
