# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 66.07


class B:
    def func(self):
        return 69


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'vfbwm': 20, 'dplqz': 3, 'zizhj': 31}


c = C()
d = c.func()
