# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'ddbrr': 29, 'jovvd': 80, 'shrbq': 16}


class B:
    def func(self):
        return 39.84


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 6


c = C()
d = c.func()
