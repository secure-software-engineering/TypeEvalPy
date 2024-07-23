# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'bxfym'


class B:
    def func(self):
        return (47, 77, 99)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 28.3


c = C()
d = c.func()
