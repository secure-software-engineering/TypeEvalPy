# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (35, 11, 21)


class B:
    def func(self):
        return {'wyjrk': 18, 'pmdsc': 49, 'syvtr': 27}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 94.87


c = C()
d = c.func()
