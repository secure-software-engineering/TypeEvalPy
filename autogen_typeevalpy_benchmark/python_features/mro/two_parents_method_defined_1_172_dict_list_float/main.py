# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'ukbzg': 61, 'tlihb': 56, 'tpsbw': 67}


class B:
    def func(self):
        return [45, 98, 49]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 27.71


c = C()
d = c.func()
