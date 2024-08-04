# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return (72, 91, 24)


class B:
    def __init__(self):
        pass

    def func(self):
        return {'wbevh': 93, 'nbjhf': 32, 'gjqlz': 73}


class C(A, B):
    pass


c = C()
d = c.func()
