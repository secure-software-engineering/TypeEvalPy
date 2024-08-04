# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [98, 80, 14]


class B:
    def func(self):
        return {'tdxgc': 4, 'psine': 32, 'wbnka': 92}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 33.71


c = C()
d = c.func()
