# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 49


class B:
    def func(self):
        return 'pplny'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 25.18


c = C()
d = c.func()
