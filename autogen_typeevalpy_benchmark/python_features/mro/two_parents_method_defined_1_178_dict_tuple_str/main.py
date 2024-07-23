# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'jeibv': 8, 'rthth': 25, 'gjzqi': 95}


class B:
    def func(self):
        return (11, 35, 28)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'psbla'


c = C()
d = c.func()
