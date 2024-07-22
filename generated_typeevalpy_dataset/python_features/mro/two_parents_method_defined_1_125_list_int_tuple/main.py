# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [53, 2, 97]


class B:
    def func(self):
        return 75


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (48, 16, 60)


c = C()
d = c.func()
