# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [22, 33, 4]


class B:
    def func(self):
        return {'tgaha': 79, 'tlmke': 29, 'zujxc': 10}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 67


c = C()
d = c.func()
