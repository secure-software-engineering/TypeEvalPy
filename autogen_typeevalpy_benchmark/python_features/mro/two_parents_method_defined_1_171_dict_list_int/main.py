# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'qtqgw': 7, 'jgaix': 75, 'wsdez': 64}


class B:
    def func(self):
        return [27, 56, 66]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 25


c = C()
d = c.func()
