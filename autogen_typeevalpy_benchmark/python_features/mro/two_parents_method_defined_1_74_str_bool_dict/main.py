# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'uqofc'


class B:
    def func(self):
        return True


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'dtptv': 72, 'dzvsi': 70, 'qkvjg': 52}


c = C()
d = c.func()
