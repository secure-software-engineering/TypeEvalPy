# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return False


class B:
    def func(self):
        return (42, 17, 61)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'fwuwg': 2, 'bctin': 15, 'excsn': 56}


c = C()
d = c.func()
