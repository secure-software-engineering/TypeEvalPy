# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 59


class B:
    def func(self):
        return (82, 33, 65)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [73, 85, 22]


c = C()
d = c.func()
