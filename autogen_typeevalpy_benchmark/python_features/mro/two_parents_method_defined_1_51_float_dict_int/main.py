# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 80.27


class B:
    def func(self):
        return {'koblb': 47, 'ikrzw': 53, 'drlel': 16}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 47


c = C()
d = c.func()
