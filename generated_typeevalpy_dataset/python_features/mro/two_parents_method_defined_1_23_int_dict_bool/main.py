# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 55


class B:
    def func(self):
        return {'gluro': 3, 'mgjpc': 43, 'vjdch': 83}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return True


c = C()
d = c.func()
