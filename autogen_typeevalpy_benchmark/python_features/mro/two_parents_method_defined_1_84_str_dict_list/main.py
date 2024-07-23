# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'qmvkg'


class B:
    def func(self):
        return {'xwkkz': 94, 'pzdwh': 75, 'ysyku': 82}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [18, 40, 30]


c = C()
d = c.func()
