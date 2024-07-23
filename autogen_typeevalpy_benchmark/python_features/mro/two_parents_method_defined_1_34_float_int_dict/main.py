# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 89.92


class B:
    def func(self):
        return 51


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'hakcy': 61, 'afugd': 21, 'uxsvj': 87}


c = C()
d = c.func()
