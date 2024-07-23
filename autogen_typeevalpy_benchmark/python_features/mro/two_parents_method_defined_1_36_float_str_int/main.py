# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 33.84


class B:
    def func(self):
        return 'rljmz'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 97


c = C()
d = c.func()
