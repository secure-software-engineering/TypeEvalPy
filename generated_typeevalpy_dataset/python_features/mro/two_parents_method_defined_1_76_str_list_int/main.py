# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'rfdui'


class B:
    def func(self):
        return [81, 15, 98]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 69


c = C()
d = c.func()
