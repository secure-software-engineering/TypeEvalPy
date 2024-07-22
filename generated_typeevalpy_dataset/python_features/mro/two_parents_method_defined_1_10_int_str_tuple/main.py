# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 19


class B:
    def func(self):
        return 'zaxpu'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (73, 96, 5)


c = C()
d = c.func()
