# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 42


class B:
    def func(self):
        return {'hyggu': 75, 'rouep': 53, 'fcfot': 46}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [9, 81, 100]


c = C()
d = c.func()
