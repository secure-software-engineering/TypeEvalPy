# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [47, 58, 37]


class B:
    def func(self):
        return (28, 62, 43)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'zwnhn': 86, 'fyudz': 36, 'uyqjn': 41}


c = C()
d = c.func()
