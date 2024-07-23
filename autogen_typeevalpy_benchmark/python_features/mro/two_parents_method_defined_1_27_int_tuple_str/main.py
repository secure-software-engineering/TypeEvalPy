# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 44


class B:
    def func(self):
        return (50, 98, 65)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'gsasw'


c = C()
d = c.func()
