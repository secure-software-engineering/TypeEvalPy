# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 60.81


class B:
    def func(self):
        return {'kyibb': 94, 'hszpz': 16, 'btcue': 61}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (92, 21, 95)


c = C()
d = c.func()
