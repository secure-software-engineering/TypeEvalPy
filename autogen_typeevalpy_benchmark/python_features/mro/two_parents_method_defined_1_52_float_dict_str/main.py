# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 92.64


class B:
    def func(self):
        return {'raesv': 29, 'yrdep': 95, 'onpfe': 44}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'siipz'


c = C()
d = c.func()
