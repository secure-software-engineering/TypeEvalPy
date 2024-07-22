# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [47, 3, 60]


class B:
    def func(self):
        return 'efhoe'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return False


c = C()
d = c.func()