# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'hqpkq': 74, 'xgnps': 92, 'lzvdo': 2}


class B:
    def func(self):
        return 'yndxe'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 36.99


c = C()
d = c.func()
