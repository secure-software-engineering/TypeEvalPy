# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 22.89


class B:
    def func(self):
        return {'cwrzo': 39, 'zbjcl': 86, 'cvcpj': 50}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 33


c = C()
d = c.func()
