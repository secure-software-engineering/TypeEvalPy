# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [19, 7, 54]


class B:
    def func(self):
        return 77.27


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'ediuz': 29, 'huofo': 19, 'nvlid': 49}


c = C()
d = c.func()
