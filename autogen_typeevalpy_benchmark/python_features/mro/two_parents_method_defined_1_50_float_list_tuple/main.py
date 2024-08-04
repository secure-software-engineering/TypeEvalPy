# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 67.08


class B:
    def func(self):
        return [47, 80, 34]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (2, 18, 94)


c = C()
d = c.func()
