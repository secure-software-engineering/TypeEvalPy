# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [37, 94, 34]


class B:
    def func(self):
        return (40, 14, 45)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return False


c = C()
d = c.func()
