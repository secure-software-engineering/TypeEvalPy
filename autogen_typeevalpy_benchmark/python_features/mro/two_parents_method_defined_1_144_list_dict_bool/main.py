# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [55, 46, 69]


class B:
    def func(self):
        return {'dgacj': 37, 'cbauf': 1, 'lptef': 94}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return False


c = C()
d = c.func()
