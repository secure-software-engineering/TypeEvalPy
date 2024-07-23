# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'lnfgx'


class B:
    def func(self):
        return (6, 8, 2)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [68, 59, 60]


c = C()
d = c.func()
