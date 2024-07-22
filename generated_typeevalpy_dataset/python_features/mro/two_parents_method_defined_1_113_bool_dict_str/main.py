# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return {'fdzrf': 72, 'zrzvn': 41, 'ckfpy': 24}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'mxbzg'


c = C()
d = c.func()
