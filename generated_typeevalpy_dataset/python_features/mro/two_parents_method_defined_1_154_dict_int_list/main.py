# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'zddhy': 98, 'ojdfn': 32, 'hibxo': 32}


class B:
    def func(self):
        return 92


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [15, 46, 83]


c = C()
d = c.func()
