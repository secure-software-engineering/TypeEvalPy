# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 82


class B:
    def func(self):
        return {'gsjqg': 91, 'etrvt': 75, 'pajos': 80}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'bvygf'


c = C()
d = c.func()
