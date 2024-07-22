# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 67


class B:
    def func(self):
        return {'uwzwq': 3, 'zyoau': 22, 'vaayk': 50}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 61.19


c = C()
d = c.func()
