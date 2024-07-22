# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [12, 8, 43]


class B:
    def func(self):
        return {'thixy': 30, 'biqwl': 24, 'ehqjr': 14}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (44, 99, 10)


c = C()
d = c.func()
