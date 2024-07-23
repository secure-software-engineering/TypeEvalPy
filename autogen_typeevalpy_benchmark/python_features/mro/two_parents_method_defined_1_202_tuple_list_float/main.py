# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (18, 38, 1)


class B:
    def func(self):
        return [18, 31, 100]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 64.84


c = C()
d = c.func()
