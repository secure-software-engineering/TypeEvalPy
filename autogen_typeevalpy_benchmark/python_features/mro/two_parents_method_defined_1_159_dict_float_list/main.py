# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'zbgio': 94, 'rtnqu': 79, 'ugdix': 96}


class B:
    def func(self):
        return 51.2


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [52, 38, 46]


c = C()
d = c.func()
