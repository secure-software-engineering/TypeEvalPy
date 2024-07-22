# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'dsqtj': 11, 'mcant': 35, 'hbvef': 97}


class B:
    def func(self):
        return (37, 65, 77)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 93.99


c = C()
d = c.func()
