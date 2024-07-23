# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 30.08


class B:
    def func(self):
        return 'fdaid'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (7, 73, 61)


c = C()
d = c.func()
