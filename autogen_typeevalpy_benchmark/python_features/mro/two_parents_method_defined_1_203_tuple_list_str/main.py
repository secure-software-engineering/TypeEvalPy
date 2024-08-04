# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (57, 96, 26)


class B:
    def func(self):
        return [1, 70, 61]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'srwgh'


c = C()
d = c.func()
