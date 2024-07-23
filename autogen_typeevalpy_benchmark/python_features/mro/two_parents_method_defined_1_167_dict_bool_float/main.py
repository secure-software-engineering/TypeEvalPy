# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'otvkb': 15, 'uhbpm': 67, 'jjrnq': 94}


class B:
    def func(self):
        return True


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 46.68


c = C()
d = c.func()
