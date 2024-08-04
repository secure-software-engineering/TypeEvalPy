# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 88.52


class B:
    def func(self):
        return 83


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (7, 38, 94)


c = C()
d = c.func()
