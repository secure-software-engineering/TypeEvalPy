# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'vrcrn': 47, 'rmuuo': 53, 'tgqem': 40}


class B:
    def func(self):
        return 'milan'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [57, 100, 65]


c = C()
d = c.func()
