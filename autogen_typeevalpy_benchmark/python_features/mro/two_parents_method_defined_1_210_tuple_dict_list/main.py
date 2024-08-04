# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (39, 39, 18)


class B:
    def func(self):
        return {'zdyvp': 65, 'vnusl': 41, 'mvypv': 80}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [56, 25, 47]


c = C()
d = c.func()
