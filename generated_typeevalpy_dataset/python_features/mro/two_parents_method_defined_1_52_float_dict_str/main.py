# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 10.06


class B:
    def func(self):
        return {'xkhgk': 73, 'dflzr': 83, 'cfzsp': 29}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'mgozm'


c = C()
d = c.func()
