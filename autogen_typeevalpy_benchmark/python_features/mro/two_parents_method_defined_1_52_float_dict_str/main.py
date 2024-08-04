# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 66.89


class B:
    def func(self):
        return {'rdvfr': 75, 'wzdhr': 77, 'hyrmx': 34}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'yxjli'


c = C()
d = c.func()
