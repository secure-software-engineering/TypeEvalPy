# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'sszmp'


class B:
    def func(self):
        return 7


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'moomw': 2, 'gspjn': 81, 'thksj': 44}


c = C()
d = c.func()
