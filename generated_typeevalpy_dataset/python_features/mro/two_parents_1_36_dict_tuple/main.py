# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return {'njhdp': 46, 'radin': 64, 'hxfen': 39}


class B:
    def __init__(self):
        pass

    def func(self):
        return (77, 16, 22)


class C(A, B):
    pass


c = C()
d = c.func()
