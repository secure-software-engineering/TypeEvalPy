# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 16.81


class B:
    def func(self):
        return [73, 41, 31]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'udyml': 93, 'pmyux': 21, 'atqef': 86}


c = C()
d = c.func()
