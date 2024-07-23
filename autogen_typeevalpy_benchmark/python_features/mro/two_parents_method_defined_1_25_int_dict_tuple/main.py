# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 35


class B:
    def func(self):
        return {'tjrkc': 19, 'jpkjv': 49, 'rmskw': 21}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (46, 8, 98)


c = C()
d = c.func()
