# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 90.06


class B:
    def func(self):
        return (29, 98, 76)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'grlai'


c = C()
d = c.func()
