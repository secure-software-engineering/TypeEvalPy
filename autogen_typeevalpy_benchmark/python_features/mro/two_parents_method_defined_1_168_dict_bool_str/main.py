# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'sxxku': 60, 'jjzpz': 77, 'hvtla': 97}


class B:
    def func(self):
        return True


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'hljbe'


c = C()
d = c.func()
