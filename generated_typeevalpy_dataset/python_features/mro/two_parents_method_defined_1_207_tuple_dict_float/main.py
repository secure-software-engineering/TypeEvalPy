# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (56, 10, 25)


class B:
    def func(self):
        return {'fppor': 4, 'ynzda': 82, 'opixq': 38}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 5.38


c = C()
d = c.func()
