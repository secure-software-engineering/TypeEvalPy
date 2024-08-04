# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 71


class B:
    def func(self):
        return True


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'uobyr': 56, 'bkalr': 3, 'tmuqe': 6}


c = C()
d = c.func()
