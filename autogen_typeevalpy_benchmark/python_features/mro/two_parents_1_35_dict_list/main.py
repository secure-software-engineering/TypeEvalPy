# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return {'mfkpp': 14, 'vxvzv': 35, 'acehk': 12}


class B:
    def __init__(self):
        pass

    def func(self):
        return [53, 91, 22]


class C(A, B):
    pass


c = C()
d = c.func()
