# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'uiwct': 3, 'ztjsh': 2, 'emews': 10}


class B:
    def func(self):
        return 'xgkms'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (13, 27, 66)


c = C()
d = c.func()
