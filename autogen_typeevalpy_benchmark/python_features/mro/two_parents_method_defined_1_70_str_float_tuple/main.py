# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'udefb'


class B:
    def func(self):
        return 46.49


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (84, 59, 76)


c = C()
d = c.func()
