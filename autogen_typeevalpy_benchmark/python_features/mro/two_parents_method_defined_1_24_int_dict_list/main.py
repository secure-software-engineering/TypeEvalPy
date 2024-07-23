# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 11


class B:
    def func(self):
        return {'rddtc': 41, 'tdjtl': 4, 'ypqnr': 70}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [61, 91, 8]


c = C()
d = c.func()
