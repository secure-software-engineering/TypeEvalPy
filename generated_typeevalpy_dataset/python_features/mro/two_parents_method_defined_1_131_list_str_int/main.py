# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [48, 81, 12]


class B:
    def func(self):
        return 'jzzan'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 32


c = C()
d = c.func()
