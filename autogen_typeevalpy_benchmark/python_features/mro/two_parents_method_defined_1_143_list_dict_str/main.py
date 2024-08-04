# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [84, 35, 77]


class B:
    def func(self):
        return {'bfyzg': 87, 'fjaus': 98, 'dtrfb': 92}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'kwkeg'


c = C()
d = c.func()
