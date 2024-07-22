# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [33, 52, 81]


class B:
    def func(self):
        return {'wskvf': 49, 'shqba': 26, 'uldrm': 33}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 96


c = C()
d = c.func()
