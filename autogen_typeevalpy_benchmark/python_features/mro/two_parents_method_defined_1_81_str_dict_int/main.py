# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'ugwpt'


class B:
    def func(self):
        return {'silvq': 5, 'hapda': 72, 'iekjm': 65}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 85


c = C()
d = c.func()
