# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 87


class B:
    def func(self):
        return {'btrft': 48, 'kckmz': 13, 'aabgs': 15}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (51, 31, 94)


c = C()
d = c.func()
