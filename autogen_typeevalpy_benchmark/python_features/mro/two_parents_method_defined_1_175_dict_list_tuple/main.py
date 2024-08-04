# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'nmfpj': 28, 'pegop': 80, 'gmkvj': 65}


class B:
    def func(self):
        return [36, 68, 14]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (16, 59, 20)


c = C()
d = c.func()
