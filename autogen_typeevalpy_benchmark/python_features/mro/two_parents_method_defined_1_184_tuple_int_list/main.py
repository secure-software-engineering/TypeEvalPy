# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (7, 19, 28)


class B:
    def func(self):
        return 86


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [82, 22, 39]


c = C()
d = c.func()
