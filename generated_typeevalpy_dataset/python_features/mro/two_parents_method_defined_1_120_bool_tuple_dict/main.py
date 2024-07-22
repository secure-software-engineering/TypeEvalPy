# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return False


class B:
    def func(self):
        return (38, 35, 49)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'ndidj': 18, 'omnip': 62, 'bgmha': 53}


c = C()
d = c.func()
