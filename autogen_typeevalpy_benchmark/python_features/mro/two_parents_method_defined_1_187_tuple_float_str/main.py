# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (13, 59, 66)


class B:
    def func(self):
        return 98.64


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'zmqft'


c = C()
d = c.func()
