# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'lbgol': 21, 'zpsoa': 72, 'edgcf': 11}


class B:
    def func(self):
        return (41, 79, 89)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'wxtiy'


c = C()
d = c.func()
