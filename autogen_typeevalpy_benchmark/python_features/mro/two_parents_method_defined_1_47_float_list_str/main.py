# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 15.56


class B:
    def func(self):
        return [37, 5, 42]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'hykcy'


c = C()
d = c.func()
