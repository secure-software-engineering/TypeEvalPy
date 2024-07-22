# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (58, 35, 34)


class B:
    def func(self):
        return {'rvxop': 54, 'yowgp': 9, 'hbrai': 73}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 22


c = C()
d = c.func()
