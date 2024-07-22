# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [2, 15, 23]


class B:
    def func(self):
        return 91.69


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'rpnwr'


c = C()
d = c.func()
