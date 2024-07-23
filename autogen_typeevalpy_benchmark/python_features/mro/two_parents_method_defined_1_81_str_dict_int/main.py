# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'imvvp'


class B:
    def func(self):
        return {'ihlah': 91, 'dovsk': 99, 'nupoc': 31}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 9


c = C()
d = c.func()
