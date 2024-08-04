# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return [98, 59, 16]


class B:
    def __init__(self):
        pass

    def func(self):
        return {'nequn': 8, 'bqhvl': 76, 'bhxqe': 52}


class C(A, B):
    pass


c = C()
d = c.func()
