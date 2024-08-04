# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return (29, 2, 71)


class B:
    def __init__(self):
        pass

    def func(self):
        return 92.49


class C(A, B):
    pass


c = C()
d = c.func()
