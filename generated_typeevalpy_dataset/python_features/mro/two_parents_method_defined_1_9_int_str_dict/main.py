# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 85


class B:
    def func(self):
        return 'evoog'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'wsrqi': 95, 'rtnps': 9, 'efmvv': 32}


c = C()
d = c.func()
