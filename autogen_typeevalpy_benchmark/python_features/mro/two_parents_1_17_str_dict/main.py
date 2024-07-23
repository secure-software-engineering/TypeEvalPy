# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return 'fjryj'


class B:
    def __init__(self):
        pass

    def func(self):
        return {'rdcpy': 11, 'xlaqs': 55, 'bqrpy': 83}


class C(A, B):
    pass


c = C()
d = c.func()
