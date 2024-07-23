# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'gfrsq'


class B:
    def func(self):
        return (78, 90, 49)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'dwqlb': 45, 'lxgcr': 63, 'acvgp': 62}


c = C()
d = c.func()
