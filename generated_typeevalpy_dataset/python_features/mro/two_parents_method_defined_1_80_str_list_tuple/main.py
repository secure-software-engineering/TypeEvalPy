# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'mpnda'


class B:
    def func(self):
        return [62, 8, 12]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (98, 61, 10)


c = C()
d = c.func()
