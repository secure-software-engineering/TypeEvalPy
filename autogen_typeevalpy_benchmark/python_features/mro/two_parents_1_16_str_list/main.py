# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return 'pqtik'


class B:
    def __init__(self):
        pass

    def func(self):
        return [28, 97, 92]


class C(A, B):
    pass


c = C()
d = c.func()
