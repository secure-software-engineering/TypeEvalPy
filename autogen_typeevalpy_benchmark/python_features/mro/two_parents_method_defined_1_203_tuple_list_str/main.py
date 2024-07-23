# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (22, 57, 39)


class B:
    def func(self):
        return [35, 61, 41]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'qtcxc'


c = C()
d = c.func()
