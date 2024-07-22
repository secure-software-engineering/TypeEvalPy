# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'gfnmq'


class B:
    def func(self):
        return 98.66


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'qcbma': 4, 'nhyxs': 37, 'otxzk': 70}


c = C()
d = c.func()
