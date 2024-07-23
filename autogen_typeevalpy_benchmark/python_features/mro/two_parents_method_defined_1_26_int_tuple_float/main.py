# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 28


class B:
    def func(self):
        return (10, 89, 80)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 24.74


c = C()
d = c.func()
