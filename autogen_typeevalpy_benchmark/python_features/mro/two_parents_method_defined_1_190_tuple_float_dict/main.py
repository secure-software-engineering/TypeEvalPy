# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (40, 39, 87)


class B:
    def func(self):
        return 88.32


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'dtjhb': 90, 'zglcj': 59, 'sjrlw': 100}


c = C()
d = c.func()
