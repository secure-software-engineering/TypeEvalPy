# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 76.11


class B:
    def func(self):
        return 57


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'bwaep': 30, 'uheef': 98, 'hfduw': 5}


c = C()
d = c.func()
