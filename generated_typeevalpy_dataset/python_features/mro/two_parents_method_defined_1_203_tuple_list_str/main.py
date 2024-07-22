# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (91, 40, 53)


class B:
    def func(self):
        return [21, 7, 33]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'vtyil'


c = C()
d = c.func()
