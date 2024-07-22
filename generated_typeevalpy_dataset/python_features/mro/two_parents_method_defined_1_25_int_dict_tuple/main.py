# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 96


class B:
    def func(self):
        return {'czvcb': 56, 'cgdui': 20, 'fgdtc': 28}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (13, 43, 20)


c = C()
d = c.func()
