# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'vujox'


class B:
    def func(self):
        return 22


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [12, 36, 8]


c = C()
d = c.func()
