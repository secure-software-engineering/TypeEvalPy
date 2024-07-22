# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 75.68


class B:
    def func(self):
        return {'makdd': 25, 'jtlol': 22, 'rditq': 74}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (17, 6, 1)


c = C()
d = c.func()
