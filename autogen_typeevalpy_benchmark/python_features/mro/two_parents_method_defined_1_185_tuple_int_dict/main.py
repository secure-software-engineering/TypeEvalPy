# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (58, 23, 58)


class B:
    def func(self):
        return 98


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'hotiy': 13, 'wfpgk': 82, 'ktlte': 23}


c = C()
d = c.func()
