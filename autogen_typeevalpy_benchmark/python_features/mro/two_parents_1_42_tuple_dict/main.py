# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return (62, 3, 84)


class B:
    def __init__(self):
        pass

    def func(self):
        return {'rtbpc': 96, 'pbqig': 37, 'ugeda': 92}


class C(A, B):
    pass


c = C()
d = c.func()
