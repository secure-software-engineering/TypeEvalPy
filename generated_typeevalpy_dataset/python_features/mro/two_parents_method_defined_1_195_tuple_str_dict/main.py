# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (29, 9, 34)


class B:
    def func(self):
        return 'ulvde'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'sldbz': 30, 'chvac': 65, 'wlmmj': 18}


c = C()
d = c.func()
