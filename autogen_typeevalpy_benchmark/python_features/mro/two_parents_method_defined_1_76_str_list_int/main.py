# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'atyej'


class B:
    def func(self):
        return [50, 97, 81]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 85


c = C()
d = c.func()
