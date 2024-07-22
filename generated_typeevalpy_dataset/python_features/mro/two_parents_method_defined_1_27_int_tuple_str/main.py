# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 64


class B:
    def func(self):
        return (88, 61, 15)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'mujqm'


c = C()
d = c.func()
