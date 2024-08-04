# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 85


class B:
    def func(self):
        return (99, 62, 72)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 75.71


c = C()
d = c.func()
