# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 47


class B:
    def func(self):
        return 52.27


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [71, 97, 78]


c = C()
d = c.func()
