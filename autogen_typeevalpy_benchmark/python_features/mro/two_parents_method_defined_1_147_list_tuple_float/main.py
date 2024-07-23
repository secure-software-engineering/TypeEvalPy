# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [80, 80, 61]


class B:
    def func(self):
        return (71, 11, 33)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 93.16


c = C()
d = c.func()
