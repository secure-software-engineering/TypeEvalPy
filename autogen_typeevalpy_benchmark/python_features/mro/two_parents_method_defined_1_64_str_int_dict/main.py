# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'evahz'


class B:
    def func(self):
        return 42


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'skthq': 22, 'xdixc': 11, 'drbrc': 45}


c = C()
d = c.func()
