# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return False


class B:
    def func(self):
        return [29, 7, 13]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (45, 84, 24)


c = C()
d = c.func()
