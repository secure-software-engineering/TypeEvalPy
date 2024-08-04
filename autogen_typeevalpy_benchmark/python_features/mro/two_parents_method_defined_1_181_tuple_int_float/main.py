# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (71, 9, 85)


class B:
    def func(self):
        return 60


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 77.67


c = C()
d = c.func()
