# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (62, 32, 15)


class B:
    def func(self):
        return 94


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'gfayq'


c = C()
d = c.func()
