# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'vfkzx'


class B:
    def func(self):
        return {'pqkcp': 48, 'axneu': 28, 'dwose': 59}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (41, 42, 87)


c = C()
d = c.func()
