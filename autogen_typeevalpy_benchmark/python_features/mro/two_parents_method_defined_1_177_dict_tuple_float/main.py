# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'uaqsp': 13, 'qkbmo': 63, 'gtfta': 59}


class B:
    def func(self):
        return (24, 27, 66)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 14.25


c = C()
d = c.func()
