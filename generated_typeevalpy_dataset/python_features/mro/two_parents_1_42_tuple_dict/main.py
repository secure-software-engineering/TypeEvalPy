# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return (19, 74, 69)


class B:
    def __init__(self):
        pass

    def func(self):
        return {'wxyxw': 15, 'bdzii': 32, 'urryl': 94}


class C(A, B):
    pass


c = C()
d = c.func()
