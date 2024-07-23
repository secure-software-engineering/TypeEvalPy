# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (29, 27, 40)


class B:
    def func(self):
        return 7.55


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [99, 84, 56]


c = C()
d = c.func()
