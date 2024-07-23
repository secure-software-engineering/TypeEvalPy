# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (96, 97, 98)


class B:
    def func(self):
        return 96


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [76, 29, 26]


c = C()
d = c.func()
