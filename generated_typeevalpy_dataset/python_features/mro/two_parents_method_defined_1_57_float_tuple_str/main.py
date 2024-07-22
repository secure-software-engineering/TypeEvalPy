# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 13.3


class B:
    def func(self):
        return (53, 29, 44)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'emggr'


c = C()
d = c.func()
