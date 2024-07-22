# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'wurdo': 59, 'dzjxy': 57, 'ffxgp': 22}


class B:
    def func(self):
        return 67


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 85.43


c = C()
d = c.func()
