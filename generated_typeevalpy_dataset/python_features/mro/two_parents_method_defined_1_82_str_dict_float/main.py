# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'stzlv'


class B:
    def func(self):
        return {'pihie': 21, 'dgpzi': 68, 'xjkea': 98}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 78.36


c = C()
d = c.func()
