# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (52, 86, 3)


class B:
    def func(self):
        return 10.57


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'qmrwh': 7, 'exldc': 62, 'wiaos': 91}


c = C()
d = c.func()
