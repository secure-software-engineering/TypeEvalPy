# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return {'krzul': 31, 'yhwxw': 41, 'zylop': 44}


class B:
    def __init__(self):
        pass

    def func(self):
        return 89.75


class C(A, B):
    pass


c = C()
d = c.func()
