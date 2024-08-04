# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 82


class B:
    def func(self):
        return {'sasok': 39, 'jnizf': 29, 'qegrl': 59}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [6, 100, 9]


c = C()
d = c.func()
