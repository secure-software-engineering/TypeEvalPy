# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return 70


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'cgnjr': 93, 'oymvs': 68, 'ssmka': 64}


c = C()
d = c.func()
