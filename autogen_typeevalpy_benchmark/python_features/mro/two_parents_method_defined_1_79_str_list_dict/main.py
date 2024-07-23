# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'ytfkf'


class B:
    def func(self):
        return [71, 83, 34]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'uyhsr': 34, 'njbye': 47, 'zysac': 4}


c = C()
d = c.func()
