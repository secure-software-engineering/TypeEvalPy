# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'ttogx': 34, 'thkmf': 87, 'urvmk': 15}


class B:
    def func(self):
        return 'mrigf'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 17


c = C()
d = c.func()
