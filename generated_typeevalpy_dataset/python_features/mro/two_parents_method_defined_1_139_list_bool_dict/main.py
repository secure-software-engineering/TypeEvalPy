# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [35, 13, 8]


class B:
    def func(self):
        return True


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'dttdd': 27, 'bieqe': 50, 'juruk': 50}


c = C()
d = c.func()
