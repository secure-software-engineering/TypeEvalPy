# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'unjlu': 95, 'mcrft': 89, 'cmros': 57}


class B:
    def func(self):
        return (21, 44, 99)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 24.33


c = C()
d = c.func()
