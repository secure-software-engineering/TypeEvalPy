# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'cjkju': 14, 'deheq': 95, 'cwldy': 12}


class B:
    def func(self):
        return [18, 99, 85]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (26, 62, 54)


c = C()
d = c.func()
