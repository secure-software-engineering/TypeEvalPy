# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 6


class B:
    def func(self):
        return 'wgwfz'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'oxvzb': 96, 'pmkwu': 22, 'gwadq': 42}


c = C()
d = c.func()
