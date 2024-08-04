# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return {'xsjed': 87, 'mornx': 31, 'rswju': 66}


class B:
    def __init__(self):
        pass

    def func(self):
        return 'aktbw'


class C(A, B):
    pass


c = C()
d = c.func()
