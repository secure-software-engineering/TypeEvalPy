# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [5, 4, 77]


class B:
    def func(self):
        return 71.63


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 72


c = C()
d = c.func()
