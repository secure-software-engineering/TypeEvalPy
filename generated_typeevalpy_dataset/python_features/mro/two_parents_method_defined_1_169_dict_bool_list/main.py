# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'uamih': 37, 'xtiwi': 87, 'xjyev': 66}


class B:
    def func(self):
        return False


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [53, 52, 23]


c = C()
d = c.func()
