# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [49, 23, 10]


class B:
    def func(self):
        return 'jimgy'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'cocwt': 93, 'jowco': 64, 'aivbi': 68}


c = C()
d = c.func()
