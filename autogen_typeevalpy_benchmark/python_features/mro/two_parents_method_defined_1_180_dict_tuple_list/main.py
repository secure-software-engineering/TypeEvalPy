# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'cdzfb': 8, 'zbxmg': 70, 'riagz': 67}


class B:
    def func(self):
        return (71, 22, 48)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [5, 58, 76]


c = C()
d = c.func()
