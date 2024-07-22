# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (98, 66, 10)


class B:
    def func(self):
        return True


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'bqxdl': 76, 'rxcez': 23, 'reetl': 65}


c = C()
d = c.func()
