# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'lzmye': 33, 'awmlz': 7, 'hzyru': 68}


class B:
    def func(self):
        return False


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 60.55


c = C()
d = c.func()
