# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return False


class B:
    def func(self):
        return [40, 23, 19]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'zgsia': 66, 'ohgyo': 80, 'hcjjs': 54}


c = C()
d = c.func()
