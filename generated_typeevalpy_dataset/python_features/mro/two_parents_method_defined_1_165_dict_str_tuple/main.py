# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'spqqd': 19, 'uyitz': 90, 'glakx': 65}


class B:
    def func(self):
        return 'igsko'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (45, 83, 44)


c = C()
d = c.func()
