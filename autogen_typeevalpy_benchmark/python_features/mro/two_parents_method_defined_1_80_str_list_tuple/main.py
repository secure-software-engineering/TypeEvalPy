# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'pdbns'


class B:
    def func(self):
        return [21, 79, 60]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (52, 57, 7)


c = C()
d = c.func()
