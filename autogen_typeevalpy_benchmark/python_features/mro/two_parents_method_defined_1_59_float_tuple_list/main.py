# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 32.21


class B:
    def func(self):
        return (90, 90, 67)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [84, 100, 74]


c = C()
d = c.func()
