# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [99, 100, 88]


class B:
    def func(self):
        return 'vngfs'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (82, 14, 51)


c = C()
d = c.func()
