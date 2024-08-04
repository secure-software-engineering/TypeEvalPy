# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'duygv': 66, 'soemo': 33, 'tdmhv': 84}


class B:
    def func(self):
        return 97


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (50, 71, 41)


c = C()
d = c.func()
