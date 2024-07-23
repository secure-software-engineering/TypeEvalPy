# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'lrpcv'


class B:
    def func(self):
        return {'ioywd': 79, 'olchs': 4, 'veizg': 39}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 42.3


c = C()
d = c.func()
