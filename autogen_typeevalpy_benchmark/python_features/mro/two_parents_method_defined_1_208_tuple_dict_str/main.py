# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (60, 13, 63)


class B:
    def func(self):
        return {'rdgbz': 6, 'nfupr': 61, 'xghiz': 40}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'vvvrd'


c = C()
d = c.func()
