# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 86.25


class B:
    def func(self):
        return [48, 46, 73]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'wgxve': 36, 'vynap': 22, 'ssowo': 30}


c = C()
d = c.func()
