# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 33.21


class B:
    def func(self):
        return 'lglkz'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (34, 71, 71)


c = C()
d = c.func()
