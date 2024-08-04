# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 47.76


class B:
    def func(self):
        return (83, 85, 68)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'jplcv': 28, 'cnxsh': 62, 'nctal': 81}


c = C()
d = c.func()
