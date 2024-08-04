# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return {'cvlpn': 6, 'liwhq': 10, 'awkdv': 58}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (64, 43, 79)


c = C()
d = c.func()
