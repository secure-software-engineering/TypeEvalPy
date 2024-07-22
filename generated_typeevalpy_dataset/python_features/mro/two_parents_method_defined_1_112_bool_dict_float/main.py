# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return {'rhelr': 63, 'kfjbl': 15, 'vntis': 80}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 54.05


c = C()
d = c.func()
