# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 24.97


class B:
    def func(self):
        return {'ywkcg': 37, 'fuwlh': 89, 'tfxkz': 69}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [27, 6, 27]


c = C()
d = c.func()
