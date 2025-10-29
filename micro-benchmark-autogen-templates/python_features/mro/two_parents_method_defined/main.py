# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return <value1>


class B:
    def func(self):
        return <value2>


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return <value3>


c = C()
d = c.func()
A().func(); B().func()
