# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'opgvi': 38, 'nifgz': 83, 'zvofl': 8}


class B:
    def func(self):
        return (62, 12, 83)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 45


c = C()
d = c.func()
