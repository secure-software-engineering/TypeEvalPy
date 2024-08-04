# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [60, 83, 15]


class B:
    def func(self):
        return (59, 76, 44)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 41.03


c = C()
d = c.func()
