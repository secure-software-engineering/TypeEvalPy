# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (30, 79, 90)


class B:
    def func(self):
        return 'mzkcn'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'olagx': 37, 'pcqdp': 9, 'ocady': 68}


c = C()
d = c.func()
