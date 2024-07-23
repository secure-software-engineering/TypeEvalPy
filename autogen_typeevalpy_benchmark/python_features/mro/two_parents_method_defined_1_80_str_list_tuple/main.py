# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'yiyyf'


class B:
    def func(self):
        return [78, 65, 7]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (9, 40, 55)


c = C()
d = c.func()
