# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'ipnqm': 53, 'jzzxn': 33, 'cmndm': 96}


class B:
    def func(self):
        return 31.19


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'abhdp'


c = C()
d = c.func()
