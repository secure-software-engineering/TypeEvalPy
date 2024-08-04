# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'dqmaa': 29, 'qahlc': 54, 'hdjmy': 7}


class B:
    def func(self):
        return (53, 90, 30)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return False


c = C()
d = c.func()
