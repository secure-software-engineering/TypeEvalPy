# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'sohhn'


class B:
    def func(self):
        return 35.9


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'wwdba': 83, 'msbpm': 6, 'hgzcw': 31}


c = C()
d = c.func()
