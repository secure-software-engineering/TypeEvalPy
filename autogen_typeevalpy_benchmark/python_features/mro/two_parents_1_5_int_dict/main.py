# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return 20


class B:
    def __init__(self):
        pass

    def func(self):
        return {'pzhsu': 5, 'xacuk': 71, 'xgfiz': 20}


class C(A, B):
    pass


c = C()
d = c.func()
