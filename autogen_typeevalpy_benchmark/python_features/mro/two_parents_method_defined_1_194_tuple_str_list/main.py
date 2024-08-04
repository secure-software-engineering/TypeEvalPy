# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (1, 32, 84)


class B:
    def func(self):
        return 'auvkv'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [95, 35, 4]


c = C()
d = c.func()
