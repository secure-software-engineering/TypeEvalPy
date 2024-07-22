# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return 'jskic'


class B:
    def __init__(self):
        pass

    def func(self):
        return {'shgxa': 88, 'mcqrj': 73, 'pfyfm': 1}


class C(A, B):
    pass


c = C()
d = c.func()
