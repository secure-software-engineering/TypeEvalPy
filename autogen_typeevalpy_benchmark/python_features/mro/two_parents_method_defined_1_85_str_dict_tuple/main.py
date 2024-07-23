# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'yoeco'


class B:
    def func(self):
        return {'drpoe': 48, 'xueww': 57, 'midzm': 21}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (51, 70, 17)


c = C()
d = c.func()
