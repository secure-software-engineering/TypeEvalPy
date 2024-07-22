# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'ummyh'


class B:
    def func(self):
        return [32, 42, 93]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'vzcbf': 7, 'nrgrc': 70, 'dkngy': 74}


c = C()
d = c.func()
