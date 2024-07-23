# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'udsiz': 92, 'tjiji': 64, 'jckrj': 56}


class B:
    def func(self):
        return 1


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [3, 86, 99]


c = C()
d = c.func()
