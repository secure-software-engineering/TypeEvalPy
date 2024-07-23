# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'efdos'


class B:
    def func(self):
        return 65.46


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 44


c = C()
d = c.func()
