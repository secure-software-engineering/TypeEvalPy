# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'eccer': 88, 'bgruc': 66, 'fjmuc': 68}


class B:
    def func(self):
        return 20


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'pffth'


c = C()
d = c.func()
