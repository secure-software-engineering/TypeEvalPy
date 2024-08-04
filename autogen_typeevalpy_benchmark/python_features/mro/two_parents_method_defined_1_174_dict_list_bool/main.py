# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'ikrqg': 3, 'vgydv': 31, 'ogvgw': 60}


class B:
    def func(self):
        return [44, 24, 51]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return False


c = C()
d = c.func()
