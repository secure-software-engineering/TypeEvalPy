# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (92, 64, 59)


class B:
    def func(self):
        return {'wqfjj': 93, 'dpghb': 73, 'fgeeu': 66}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'khykv'


c = C()
d = c.func()
