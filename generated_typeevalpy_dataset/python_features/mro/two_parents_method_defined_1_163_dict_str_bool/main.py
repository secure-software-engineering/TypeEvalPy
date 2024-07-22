# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'ixbom': 32, 'atcmg': 88, 'dytsr': 60}


class B:
    def func(self):
        return 'eoifp'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return True


c = C()
d = c.func()
