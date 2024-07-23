# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 35


class B:
    def func(self):
        return {'qxkzi': 88, 'yuygc': 21, 'oizma': 72}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'yxtme'


c = C()
d = c.func()
