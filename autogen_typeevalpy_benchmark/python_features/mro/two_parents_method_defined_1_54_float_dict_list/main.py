# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 11.65


class B:
    def func(self):
        return {'lhbtu': 13, 'djtkq': 37, 'qnaun': 68}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [39, 70, 82]


c = C()
d = c.func()
