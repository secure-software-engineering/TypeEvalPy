# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'vqhvz'


class B:
    def func(self):
        return 54.52


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (98, 54, 85)


c = C()
d = c.func()
