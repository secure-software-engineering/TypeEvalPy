# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 49.54


class B:
    def func(self):
        return [36, 69, 30]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (52, 42, 96)


c = C()
d = c.func()
