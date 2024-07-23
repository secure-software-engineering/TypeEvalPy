# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 15.12


class B:
    def func(self):
        return {'lulmi': 46, 'qybnu': 14, 'angtu': 3}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (28, 100, 68)


c = C()
d = c.func()
