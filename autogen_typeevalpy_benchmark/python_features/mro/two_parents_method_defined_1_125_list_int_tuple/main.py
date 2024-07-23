# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [90, 89, 60]


class B:
    def func(self):
        return 35


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (73, 91, 28)


c = C()
d = c.func()
