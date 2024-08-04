# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [4, 11, 74]


class B:
    def func(self):
        return (89, 68, 24)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 63


c = C()
d = c.func()
