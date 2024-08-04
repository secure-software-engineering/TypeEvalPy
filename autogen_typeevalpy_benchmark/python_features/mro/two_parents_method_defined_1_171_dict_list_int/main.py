# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'xqxfg': 16, 'ejsbi': 24, 'ibbpk': 41}


class B:
    def func(self):
        return [69, 36, 2]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 38


c = C()
d = c.func()
