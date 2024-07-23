# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [96, 99, 8]


class B:
    def func(self):
        return 68.26


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'oqnxx': 43, 'fbqlw': 11, 'qjysk': 9}


c = C()
d = c.func()
