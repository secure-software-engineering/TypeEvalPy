# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'mkakg'


class B:
    def func(self):
        return 30.63


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (4, 79, 53)


c = C()
d = c.func()
