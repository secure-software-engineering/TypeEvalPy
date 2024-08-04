# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 37


class B:
    def func(self):
        return (46, 88, 58)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'qgvex'


c = C()
d = c.func()
