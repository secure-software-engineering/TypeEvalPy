# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [45, 10, 51]


class B:
    def func(self):
        return 78


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'ycmga'


c = C()
d = c.func()
