# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'difcs': 12, 'fqjah': 35, 'xqwsw': 69}


class B:
    def func(self):
        return 48


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [40, 30, 52]


c = C()
d = c.func()
