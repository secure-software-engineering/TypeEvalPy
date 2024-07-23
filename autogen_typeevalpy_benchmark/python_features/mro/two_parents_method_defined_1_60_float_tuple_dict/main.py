# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 65.62


class B:
    def func(self):
        return (14, 30, 83)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'mzfla': 94, 'ojuxe': 3, 'buqch': 27}


c = C()
d = c.func()
