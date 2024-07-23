# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return False


class B:
    def func(self):
        return [26, 42, 49]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (58, 40, 32)


c = C()
d = c.func()
