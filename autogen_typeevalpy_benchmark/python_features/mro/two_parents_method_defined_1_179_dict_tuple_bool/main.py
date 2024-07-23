# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'sttbw': 56, 'zbxid': 73, 'tzozp': 24}


class B:
    def func(self):
        return (98, 48, 82)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return False


c = C()
d = c.func()
