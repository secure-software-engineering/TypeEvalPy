# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'svpou'


class B:
    def func(self):
        return [68, 61, 10]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 81.23


c = C()
d = c.func()
