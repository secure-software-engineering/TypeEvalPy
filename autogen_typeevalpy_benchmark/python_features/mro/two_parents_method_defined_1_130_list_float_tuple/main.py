# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [35, 33, 83]


class B:
    def func(self):
        return 42.14


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (28, 18, 95)


c = C()
d = c.func()
