# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'uxpnk': 38, 'raizi': 44, 'ifwix': 94}


class B:
    def func(self):
        return [95, 95, 99]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'lsvtn'


c = C()
d = c.func()
