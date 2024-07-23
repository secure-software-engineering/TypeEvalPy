# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'dwpom': 89, 'qnwrw': 29, 'hizyu': 28}


class B:
    def func(self):
        return 25.52


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'cylzg'


c = C()
d = c.func()
