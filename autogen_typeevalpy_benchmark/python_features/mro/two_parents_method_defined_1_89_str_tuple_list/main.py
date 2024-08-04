# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'dwngy'


class B:
    def func(self):
        return (27, 78, 64)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [17, 1, 6]


c = C()
d = c.func()
