# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'rxicb': 50, 'beyvw': 36, 'jbbru': 70}


class B:
    def func(self):
        return 'xtbpb'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 11


c = C()
d = c.func()
