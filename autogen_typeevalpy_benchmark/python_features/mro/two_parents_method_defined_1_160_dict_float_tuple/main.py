# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'bmoml': 72, 'mqxxn': 39, 'ujdye': 6}


class B:
    def func(self):
        return 9.91


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (81, 71, 64)


c = C()
d = c.func()
