# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return False


class B:
    def func(self):
        return (74, 79, 18)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [30, 3, 90]


c = C()
d = c.func()
