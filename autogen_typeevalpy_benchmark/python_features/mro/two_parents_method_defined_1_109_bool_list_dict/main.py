# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return [55, 90, 13]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'enail': 51, 'ggdvr': 54, 'latxn': 33}


c = C()
d = c.func()
