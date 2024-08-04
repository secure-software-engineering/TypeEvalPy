# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 11


class B:
    def func(self):
        return {'mbebs': 42, 'yyjqc': 24, 'oypxb': 76}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 60.97


c = C()
d = c.func()
