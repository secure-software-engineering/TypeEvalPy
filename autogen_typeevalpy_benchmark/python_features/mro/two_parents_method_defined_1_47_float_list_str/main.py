# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 34.23


class B:
    def func(self):
        return [9, 20, 98]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'bvqky'


c = C()
d = c.func()
