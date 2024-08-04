# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'lpypr': 67, 'mhvoe': 81, 'sgvei': 33}


class B:
    def func(self):
        return 'rpgoz'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [84, 67, 40]


c = C()
d = c.func()
