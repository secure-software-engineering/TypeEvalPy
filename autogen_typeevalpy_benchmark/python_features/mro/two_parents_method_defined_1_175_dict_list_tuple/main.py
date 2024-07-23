# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'kzkdt': 84, 'alaat': 46, 'sfsmc': 2}


class B:
    def func(self):
        return [78, 84, 49]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (80, 79, 12)


c = C()
d = c.func()
