# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [13, 52, 14]


class B:
    def func(self):
        return 'iqvfq'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 64.45


c = C()
d = c.func()
