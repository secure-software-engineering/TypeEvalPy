# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (70, 3, 26)


class B:
    def func(self):
        return {'szrgz': 56, 'aazlz': 33, 'pmpfy': 78}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return False


c = C()
d = c.func()
