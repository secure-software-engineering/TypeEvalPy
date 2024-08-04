# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 36.2


class B:
    def func(self):
        return 'bvejp'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [11, 66, 56]


c = C()
d = c.func()
