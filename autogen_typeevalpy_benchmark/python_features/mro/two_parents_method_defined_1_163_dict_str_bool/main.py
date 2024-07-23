# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'giylm': 46, 'elzgm': 25, 'nzgop': 96}


class B:
    def func(self):
        return 'seqjm'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return False


c = C()
d = c.func()
