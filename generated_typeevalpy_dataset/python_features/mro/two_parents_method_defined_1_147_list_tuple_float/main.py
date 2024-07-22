# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [27, 48, 25]


class B:
    def func(self):
        return (53, 8, 46)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 79.54


c = C()
d = c.func()
