# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (98, 60, 49)


class B:
    def func(self):
        return [99, 15, 30]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 24.57


c = C()
d = c.func()
