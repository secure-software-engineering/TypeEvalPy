# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'ihkgx': 47, 'lzydy': 89, 'zbfcd': 90}


class B:
    def func(self):
        return 91.46


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return True


c = C()
d = c.func()
