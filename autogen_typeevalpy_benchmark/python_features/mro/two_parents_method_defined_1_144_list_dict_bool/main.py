# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [9, 28, 15]


class B:
    def func(self):
        return {'fcbca': 19, 'yrewd': 12, 'mmjgc': 6}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return False


c = C()
d = c.func()
