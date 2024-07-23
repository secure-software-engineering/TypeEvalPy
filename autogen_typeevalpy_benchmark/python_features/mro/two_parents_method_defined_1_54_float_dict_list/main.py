# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 9.68


class B:
    def func(self):
        return {'zxhrm': 75, 'snpsg': 18, 'gvzaa': 61}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [24, 89, 53]


c = C()
d = c.func()
