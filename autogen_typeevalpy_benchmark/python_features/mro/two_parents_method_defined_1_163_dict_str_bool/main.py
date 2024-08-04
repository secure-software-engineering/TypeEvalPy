# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'shyng': 25, 'kjumu': 31, 'bsyml': 91}


class B:
    def func(self):
        return 'eakcq'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return True


c = C()
d = c.func()
