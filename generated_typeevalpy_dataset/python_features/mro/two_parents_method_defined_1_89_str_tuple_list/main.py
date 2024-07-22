# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'pxclt'


class B:
    def func(self):
        return (47, 3, 81)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [51, 26, 40]


c = C()
d = c.func()
