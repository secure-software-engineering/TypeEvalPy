# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return False


class B:
    def func(self):
        return 36.64


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'vygkg': 42, 'dvmqz': 35, 'jtwjp': 10}


c = C()
d = c.func()
