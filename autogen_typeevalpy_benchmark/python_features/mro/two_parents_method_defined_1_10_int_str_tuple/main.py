# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 47


class B:
    def func(self):
        return 'rtrjk'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (86, 42, 2)


c = C()
d = c.func()
