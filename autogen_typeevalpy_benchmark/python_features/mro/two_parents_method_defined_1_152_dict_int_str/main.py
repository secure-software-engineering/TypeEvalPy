# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'ghfqo': 58, 'gvkct': 5, 'gepkf': 84}


class B:
    def func(self):
        return 5


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'pdfrw'


c = C()
d = c.func()
