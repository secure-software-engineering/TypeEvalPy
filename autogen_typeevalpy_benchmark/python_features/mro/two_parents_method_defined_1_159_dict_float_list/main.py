# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'uoqmv': 35, 'sivwh': 81, 'vkewu': 61}


class B:
    def func(self):
        return 29.59


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [29, 8, 5]


c = C()
d = c.func()
