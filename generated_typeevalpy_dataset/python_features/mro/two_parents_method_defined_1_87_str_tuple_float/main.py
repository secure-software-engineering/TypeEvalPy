# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'sahju'


class B:
    def func(self):
        return (20, 54, 93)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 99.85


c = C()
d = c.func()
