# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'gujhz'


class B:
    def func(self):
        return 78.32


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [85, 98, 18]


c = C()
d = c.func()
