# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (35, 39, 48)


class B:
    def func(self):
        return {'jfpvq': 40, 'jooyh': 53, 'pakky': 48}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 7.59


c = C()
d = c.func()
