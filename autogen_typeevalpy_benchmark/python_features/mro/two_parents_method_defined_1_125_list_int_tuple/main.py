# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [53, 18, 8]


class B:
    def func(self):
        return 74


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (86, 41, 17)


c = C()
d = c.func()
