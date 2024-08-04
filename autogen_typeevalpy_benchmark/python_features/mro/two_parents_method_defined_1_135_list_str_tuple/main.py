# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [96, 19, 78]


class B:
    def func(self):
        return 'dbpnu'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (52, 10, 85)


c = C()
d = c.func()
