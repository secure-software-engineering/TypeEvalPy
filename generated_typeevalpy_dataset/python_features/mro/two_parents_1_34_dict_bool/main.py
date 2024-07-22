# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return {'tyqql': 6, 'dczbq': 79, 'ymlgl': 81}


class B:
    def __init__(self):
        pass

    def func(self):
        return True


class C(A, B):
    pass


c = C()
d = c.func()
