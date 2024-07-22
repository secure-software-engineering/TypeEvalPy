# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'ergsw': 46, 'cebnb': 18, 'stukv': 43}


class B:
    def func(self):
        return [71, 2, 55]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 76.42


c = C()
d = c.func()
