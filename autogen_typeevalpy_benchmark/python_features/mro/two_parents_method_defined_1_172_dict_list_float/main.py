# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'fglyu': 30, 'vkfir': 49, 'gzhkn': 10}


class B:
    def func(self):
        return [56, 6, 24]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 84.33


c = C()
d = c.func()
