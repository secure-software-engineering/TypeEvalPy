# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 36.77


class B:
    def func(self):
        return 63


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (98, 72, 74)


c = C()
d = c.func()
