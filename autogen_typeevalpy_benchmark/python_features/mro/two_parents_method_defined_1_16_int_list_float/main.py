# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 10


class B:
    def func(self):
        return [87, 91, 85]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 23.79


c = C()
d = c.func()
