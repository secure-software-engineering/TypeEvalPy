# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'qumym': 75, 'jhcpq': 69, 'uhxei': 89}


class B:
    def func(self):
        return 64.34


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (1, 86, 46)


c = C()
d = c.func()
