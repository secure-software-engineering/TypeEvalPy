# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'xztnt'


class B:
    def func(self):
        return [39, 50, 65]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 44.82


c = C()
d = c.func()
