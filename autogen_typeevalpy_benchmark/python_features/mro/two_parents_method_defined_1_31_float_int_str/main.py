# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 26.26


class B:
    def func(self):
        return 65


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'zcede'


c = C()
d = c.func()
