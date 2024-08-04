# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 34


class B:
    def func(self):
        return {'ddjgu': 43, 'qgeue': 66, 'uxrfa': 85}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'qfsfq'


c = C()
d = c.func()
