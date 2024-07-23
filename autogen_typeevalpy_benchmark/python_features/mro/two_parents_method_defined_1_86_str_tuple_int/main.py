# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'fjood'


class B:
    def func(self):
        return (76, 56, 44)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 83


c = C()
d = c.func()
