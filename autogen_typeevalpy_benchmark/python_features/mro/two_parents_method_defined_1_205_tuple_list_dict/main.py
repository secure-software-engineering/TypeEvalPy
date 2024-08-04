# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (85, 37, 2)


class B:
    def func(self):
        return [56, 91, 35]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'xtqrr': 27, 'ljbdt': 82, 'xifpz': 50}


c = C()
d = c.func()
