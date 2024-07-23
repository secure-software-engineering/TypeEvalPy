# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'xdtjg'


class B:
    def func(self):
        return False


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'urpyo': 7, 'kflck': 73, 'bzeyi': 60}


c = C()
d = c.func()
