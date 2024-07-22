# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 66


class B:
    def func(self):
        return 'cxxgo'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [64, 68, 83]


c = C()
d = c.func()