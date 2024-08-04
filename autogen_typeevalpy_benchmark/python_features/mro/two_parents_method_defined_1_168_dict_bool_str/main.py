# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'cmlnz': 12, 'itdxe': 15, 'cheaz': 95}


class B:
    def func(self):
        return True


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'nuvpg'


c = C()
d = c.func()
