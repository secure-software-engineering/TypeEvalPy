# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [34, 20, 15]


class B:
    def func(self):
        return {'wzell': 91, 'sfbmr': 30, 'wkaon': 69}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 31.16


c = C()
d = c.func()
