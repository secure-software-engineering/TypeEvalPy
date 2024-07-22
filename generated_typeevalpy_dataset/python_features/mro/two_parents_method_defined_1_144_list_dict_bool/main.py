# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [64, 73, 75]


class B:
    def func(self):
        return {'xabew': 67, 'imner': 4, 'hteda': 77}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return True


c = C()
d = c.func()
