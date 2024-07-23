# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'yfgcy': 69, 'jaqld': 60, 'qrnii': 61}


class B:
    def func(self):
        return True


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (88, 31, 59)


c = C()
d = c.func()
