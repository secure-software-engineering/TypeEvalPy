# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 52.91


class B:
    def func(self):
        return [57, 59, 21]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 38


c = C()
d = c.func()
