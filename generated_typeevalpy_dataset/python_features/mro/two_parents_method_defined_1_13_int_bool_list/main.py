# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 84


class B:
    def func(self):
        return False


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [28, 69, 11]


c = C()
d = c.func()
