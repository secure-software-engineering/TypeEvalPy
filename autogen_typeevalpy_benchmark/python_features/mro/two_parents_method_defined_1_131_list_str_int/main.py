# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [39, 65, 26]


class B:
    def func(self):
        return 'jmquk'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 50


c = C()
d = c.func()
