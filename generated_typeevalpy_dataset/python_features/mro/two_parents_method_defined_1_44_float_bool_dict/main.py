# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 48.17


class B:
    def func(self):
        return True


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'edlfc': 54, 'fuqxi': 1, 'jqlqh': 53}


c = C()
d = c.func()
