# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'msnwr'


class B:
    def func(self):
        return True


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'kdmpd': 79, 'pwibv': 70, 'hqdyx': 74}


c = C()
d = c.func()
