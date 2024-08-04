# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (64, 40, 51)


class B:
    def func(self):
        return 68


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'ymoyc': 70, 'jtfbs': 94, 'stlwl': 3}


c = C()
d = c.func()
