# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [49, 11, 5]


class B:
    def func(self):
        return 21.77


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (20, 15, 16)


c = C()
d = c.func()
