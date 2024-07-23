# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (29, 86, 51)


class B:
    def func(self):
        return 'kltxt'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'ltusq': 64, 'feynm': 96, 'lqvml': 92}


c = C()
d = c.func()
