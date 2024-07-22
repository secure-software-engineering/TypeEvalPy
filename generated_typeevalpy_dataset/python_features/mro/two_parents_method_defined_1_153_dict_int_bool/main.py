# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'nhhtx': 19, 'akxmf': 62, 'zrznu': 93}


class B:
    def func(self):
        return 95


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return False


c = C()
d = c.func()
