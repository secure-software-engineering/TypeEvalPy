# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [26, 92, 14]


class B:
    def func(self):
        return {'lbkvx': 20, 'xythf': 13, 'rwphh': 99}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 89.34


c = C()
d = c.func()
