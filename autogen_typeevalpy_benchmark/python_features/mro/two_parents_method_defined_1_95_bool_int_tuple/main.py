# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return 24


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (100, 46, 62)


c = C()
d = c.func()
