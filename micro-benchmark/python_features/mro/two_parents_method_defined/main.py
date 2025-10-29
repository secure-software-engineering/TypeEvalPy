# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 42.5


class B:
    def func(self):
        return 42


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return "Hello from func in class C"


c = C()
d = c.func()
A().func(); B().func()
