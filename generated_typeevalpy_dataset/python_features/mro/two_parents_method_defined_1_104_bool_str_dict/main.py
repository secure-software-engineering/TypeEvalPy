# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return 'buheb'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'ahrvg': 42, 'lwgty': 44, 'qbrrq': 43}


c = C()
d = c.func()
