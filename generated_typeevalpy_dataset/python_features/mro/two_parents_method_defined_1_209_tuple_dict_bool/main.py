# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (99, 58, 22)


class B:
    def func(self):
        return {'fxrxh': 52, 'flied': 38, 'ijyqm': 87}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return True


c = C()
d = c.func()
