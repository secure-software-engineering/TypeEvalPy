# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 11.06


class B:
    def func(self):
        return False


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'sizjs': 81, 'fxcyg': 69, 'yexan': 98}


c = C()
d = c.func()
