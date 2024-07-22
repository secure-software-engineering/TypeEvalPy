# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 82


class B:
    def func(self):
        return [96, 92, 54]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'fowwf': 60, 'bvhbu': 87, 'nudbu': 23}


c = C()
d = c.func()
