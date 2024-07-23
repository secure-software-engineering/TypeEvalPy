# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 56


class B:
    def func(self):
        return [64, 28, 23]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'qyeky': 83, 'eaaxj': 75, 'sxcgs': 34}


c = C()
d = c.func()
