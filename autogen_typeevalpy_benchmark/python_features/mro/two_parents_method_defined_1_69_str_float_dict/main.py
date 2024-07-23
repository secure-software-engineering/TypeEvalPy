# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'oavha'


class B:
    def func(self):
        return 99.25


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'xdaek': 75, 'ngelr': 1, 'yljby': 1}


c = C()
d = c.func()
