# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [29, 37, 2]


class B:
    def func(self):
        return (63, 11, 99)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'itrhy': 28, 'eomvk': 64, 'ewhun': 66}


c = C()
d = c.func()
