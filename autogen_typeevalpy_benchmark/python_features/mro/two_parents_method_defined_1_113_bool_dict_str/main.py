# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return {'rguuc': 30, 'huzlt': 26, 'rvkax': 64}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'bnjxb'


c = C()
d = c.func()
