# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return 19.79


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'yddci': 98, 'efrdu': 56, 'ylsys': 72}


c = C()
d = c.func()
