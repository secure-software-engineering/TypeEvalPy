# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return False


class B:
    def func(self):
        return {'xzmsu': 73, 'cnhmp': 3, 'adcwh': 8}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 22


c = C()
d = c.func()
