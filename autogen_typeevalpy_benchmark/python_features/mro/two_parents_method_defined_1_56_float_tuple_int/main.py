# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 94.58


class B:
    def func(self):
        return (59, 53, 78)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 63


c = C()
d = c.func()
