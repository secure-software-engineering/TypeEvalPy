# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return False


class B:
    def func(self):
        return {'zoozy': 46, 'yswdm': 90, 'pekvj': 5}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [10, 70, 24]


c = C()
d = c.func()
