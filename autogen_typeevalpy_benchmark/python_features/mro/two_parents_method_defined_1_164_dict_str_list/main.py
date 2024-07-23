# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'crjua': 79, 'uasgo': 21, 'sttzu': 15}


class B:
    def func(self):
        return 'odtzz'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [1, 27, 89]


c = C()
d = c.func()
