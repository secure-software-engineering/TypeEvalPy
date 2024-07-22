# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [69, 14, 74]


class B:
    def func(self):
        return 73.59


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (92, 19, 45)


c = C()
d = c.func()
