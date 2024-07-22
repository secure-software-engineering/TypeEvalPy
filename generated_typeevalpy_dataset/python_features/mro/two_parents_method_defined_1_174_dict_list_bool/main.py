# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'zzado': 81, 'cswue': 94, 'kcdym': 34}


class B:
    def func(self):
        return [15, 42, 95]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return True


c = C()
d = c.func()
