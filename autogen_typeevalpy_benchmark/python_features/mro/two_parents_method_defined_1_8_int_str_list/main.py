# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 6


class B:
    def func(self):
        return 'nolnp'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [20, 74, 63]


c = C()
d = c.func()
