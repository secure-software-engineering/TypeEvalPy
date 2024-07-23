# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (59, 4, 100)


class B:
    def func(self):
        return {'lpkcu': 25, 'xtvus': 17, 'lxsea': 44}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'hbbvn'


c = C()
d = c.func()
