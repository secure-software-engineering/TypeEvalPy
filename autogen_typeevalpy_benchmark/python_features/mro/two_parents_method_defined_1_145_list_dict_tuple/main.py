# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [38, 97, 64]


class B:
    def func(self):
        return {'jbvrq': 9, 'fyevb': 73, 'vxewa': 11}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (60, 61, 90)


c = C()
d = c.func()
