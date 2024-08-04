# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'muzfd'


class B:
    def func(self):
        return {'cpbqd': 36, 'pndro': 60, 'woxzv': 80}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [25, 79, 67]


c = C()
d = c.func()
