# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (4, 17, 7)


class B:
    def func(self):
        return 21.39


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'idhzc': 10, 'vgkqg': 28, 'nyysf': 68}


c = C()
d = c.func()
