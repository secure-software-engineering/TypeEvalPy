# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 37


class B:
    def func(self):
        return [82, 33, 78]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (64, 79, 64)


c = C()
d = c.func()
