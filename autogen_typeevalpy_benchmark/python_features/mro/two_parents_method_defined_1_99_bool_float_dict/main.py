# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return 33.48


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'yatrs': 92, 'byxus': 24, 'onsnh': 36}


c = C()
d = c.func()
