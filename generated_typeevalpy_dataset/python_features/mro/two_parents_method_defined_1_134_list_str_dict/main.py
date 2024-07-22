# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [10, 75, 46]


class B:
    def func(self):
        return 'fqfcb'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'nmfzz': 66, 'ykpdg': 55, 'ejvva': 76}


c = C()
d = c.func()
