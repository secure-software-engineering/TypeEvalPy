# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [86, 16, 40]


class B:
    def func(self):
        return {'dynmh': 31, 'eeuzu': 23, 'tuaci': 32}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 17


c = C()
d = c.func()
