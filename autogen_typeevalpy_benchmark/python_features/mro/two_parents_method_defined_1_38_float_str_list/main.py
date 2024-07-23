# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 72.84


class B:
    def func(self):
        return 'fxtrw'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [76, 31, 90]


c = C()
d = c.func()
