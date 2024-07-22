# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'tlmve'


class B:
    def func(self):
        return {'tfqgv': 73, 'rkice': 71, 'dcorg': 40}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return False


c = C()
d = c.func()
