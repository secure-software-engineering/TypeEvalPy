# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return {'acxnb': 73, 'zteur': 23, 'zkpmx': 96}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (72, 95, 89)


c = C()
d = c.func()
