# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'peyxb': 17, 'htldz': 29, 'zsoee': 3}


class B:
    def func(self):
        return 50.26


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 73


c = C()
d = c.func()
