# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 29


class B:
    def func(self):
        return (4, 86, 37)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'iszjr': 59, 'qvqfp': 56, 'fulnr': 48}


c = C()
d = c.func()
