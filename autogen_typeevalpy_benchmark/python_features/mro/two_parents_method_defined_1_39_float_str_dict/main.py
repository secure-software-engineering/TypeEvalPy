# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 50.07


class B:
    def func(self):
        return 'hrrwk'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'fetfd': 31, 'ppovr': 23, 'xnplf': 27}


c = C()
d = c.func()
