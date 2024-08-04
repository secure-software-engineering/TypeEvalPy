# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [60, 41, 24]


class B:
    def func(self):
        return True


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'zkjue': 74, 'ghzjy': 13, 'lzhnx': 41}


c = C()
d = c.func()
