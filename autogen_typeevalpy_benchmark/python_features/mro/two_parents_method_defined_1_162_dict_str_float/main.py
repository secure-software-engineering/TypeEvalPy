# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'exgeh': 61, 'fqnnm': 23, 'xijuk': 42}


class B:
    def func(self):
        return 'nwdeb'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 26.44


c = C()
d = c.func()
