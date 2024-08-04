# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (35, 57, 14)


class B:
    def func(self):
        return [77, 98, 96]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 30


c = C()
d = c.func()
