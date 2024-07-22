# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (88, 53, 67)


class B:
    def func(self):
        return 83.5


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 68


c = C()
d = c.func()
