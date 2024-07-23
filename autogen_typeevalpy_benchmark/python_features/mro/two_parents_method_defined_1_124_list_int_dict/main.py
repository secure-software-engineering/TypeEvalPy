# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [56, 52, 62]


class B:
    def func(self):
        return 6


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'nmbix': 57, 'nrsod': 77, 'opewc': 35}


c = C()
d = c.func()
