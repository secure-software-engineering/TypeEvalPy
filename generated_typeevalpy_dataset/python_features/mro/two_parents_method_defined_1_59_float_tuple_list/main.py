# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 84.77


class B:
    def func(self):
        return (27, 32, 24)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [87, 50, 47]


c = C()
d = c.func()
