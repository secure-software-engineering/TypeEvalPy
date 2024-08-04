# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'fkzti': 41, 'eiexk': 35, 'zygcj': 12}


class B:
    def func(self):
        return 69.83


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (70, 28, 24)


c = C()
d = c.func()
