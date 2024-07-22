# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 91.33


class B:
    def func(self):
        return (48, 61, 10)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 67


c = C()
d = c.func()
