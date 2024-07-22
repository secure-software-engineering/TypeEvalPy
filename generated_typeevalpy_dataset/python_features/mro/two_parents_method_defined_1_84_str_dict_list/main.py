# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'xxosk'


class B:
    def func(self):
        return {'ixwqc': 58, 'iwqly': 4, 'ahxzl': 53}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [56, 13, 29]


c = C()
d = c.func()
