# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return (30, 24, 57)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [87, 15, 31]


c = C()
d = c.func()
