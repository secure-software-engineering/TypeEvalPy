# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (74, 13, 54)


class B:
    def func(self):
        return [41, 22, 57]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 67.72


c = C()
d = c.func()
