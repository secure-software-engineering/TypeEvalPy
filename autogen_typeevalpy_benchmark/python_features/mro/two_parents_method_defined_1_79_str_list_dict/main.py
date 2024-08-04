# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'gdsrm'


class B:
    def func(self):
        return [7, 56, 93]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'uimwu': 27, 'futoa': 29, 'wmsab': 61}


c = C()
d = c.func()
