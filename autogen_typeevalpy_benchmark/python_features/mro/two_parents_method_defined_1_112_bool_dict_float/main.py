# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return False


class B:
    def func(self):
        return {'uyldw': 39, 'fcfew': 6, 'agtgq': 47}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 64.37


c = C()
d = c.func()
