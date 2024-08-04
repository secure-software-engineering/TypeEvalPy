# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return 'csewl'


class B:
    def __init__(self):
        pass

    def func(self):
        return (20, 75, 24)


class C(A, B):
    pass


c = C()
d = c.func()
