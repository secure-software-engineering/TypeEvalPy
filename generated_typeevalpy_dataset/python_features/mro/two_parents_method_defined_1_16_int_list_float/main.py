# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 75


class B:
    def func(self):
        return [14, 44, 8]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 27.39


c = C()
d = c.func()
