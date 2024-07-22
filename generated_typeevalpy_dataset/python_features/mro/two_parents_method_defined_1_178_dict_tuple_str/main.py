# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'lvrua': 19, 'yngfw': 42, 'nvdeh': 7}


class B:
    def func(self):
        return (32, 100, 48)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'kshnp'


c = C()
d = c.func()
