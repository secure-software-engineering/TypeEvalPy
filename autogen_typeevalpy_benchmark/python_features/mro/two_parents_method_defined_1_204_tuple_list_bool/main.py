# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (97, 6, 2)


class B:
    def func(self):
        return [89, 22, 86]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return False


c = C()
d = c.func()
