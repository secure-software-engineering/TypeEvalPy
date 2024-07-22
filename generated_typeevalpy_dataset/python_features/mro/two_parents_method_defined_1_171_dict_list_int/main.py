# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'zdsjg': 5, 'hsbbg': 24, 'rjcgd': 8}


class B:
    def func(self):
        return [33, 16, 63]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 26


c = C()
d = c.func()
