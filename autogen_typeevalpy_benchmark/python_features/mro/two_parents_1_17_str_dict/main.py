# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return 'ncsow'


class B:
    def __init__(self):
        pass

    def func(self):
        return {'kegit': 47, 'tfain': 88, 'tgapz': 21}


class C(A, B):
    pass


c = C()
d = c.func()
