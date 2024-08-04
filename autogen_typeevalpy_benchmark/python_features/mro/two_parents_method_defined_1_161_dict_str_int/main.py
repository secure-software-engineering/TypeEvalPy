# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'cdyyo': 63, 'nazfi': 9, 'yrkrm': 1}


class B:
    def func(self):
        return 'hqjzt'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 71


c = C()
d = c.func()
