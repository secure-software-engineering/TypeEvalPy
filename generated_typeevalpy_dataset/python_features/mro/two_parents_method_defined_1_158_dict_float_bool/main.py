# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'qtqsq': 14, 'lmebm': 88, 'lktlx': 58}


class B:
    def func(self):
        return 38.41


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return True


c = C()
d = c.func()