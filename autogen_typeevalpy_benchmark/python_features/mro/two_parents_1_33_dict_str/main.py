# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return {'svzxz': 19, 'wpfsd': 99, 'oboni': 87}


class B:
    def __init__(self):
        pass

    def func(self):
        return 'vpuys'


class C(A, B):
    pass


c = C()
d = c.func()
