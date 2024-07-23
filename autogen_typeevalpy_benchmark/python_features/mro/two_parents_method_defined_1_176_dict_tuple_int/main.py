# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'hfqcp': 70, 'nwtsk': 47, 'kdghd': 89}


class B:
    def func(self):
        return (5, 70, 47)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 53


c = C()
d = c.func()
