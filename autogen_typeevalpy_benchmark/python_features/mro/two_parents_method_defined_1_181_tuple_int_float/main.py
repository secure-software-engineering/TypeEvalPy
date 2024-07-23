# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (20, 56, 87)


class B:
    def func(self):
        return 67


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 13.61


c = C()
d = c.func()
