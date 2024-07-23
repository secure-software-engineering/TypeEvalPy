# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (70, 29, 51)


class B:
    def func(self):
        return {'blfhw': 92, 'tvmnc': 13, 'afvtm': 16}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 15


c = C()
d = c.func()
