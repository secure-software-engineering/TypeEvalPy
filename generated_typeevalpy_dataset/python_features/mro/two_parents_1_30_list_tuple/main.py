# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return [88, 97, 40]


class B:
    def __init__(self):
        pass

    def func(self):
        return (82, 37, 18)


class C(A, B):
    pass


c = C()
d = c.func()
