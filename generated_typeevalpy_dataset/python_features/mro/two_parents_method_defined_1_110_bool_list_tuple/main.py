# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return False


class B:
    def func(self):
        return [51, 90, 57]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (89, 13, 90)


c = C()
d = c.func()
