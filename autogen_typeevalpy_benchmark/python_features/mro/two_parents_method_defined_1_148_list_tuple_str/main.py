# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [26, 27, 17]


class B:
    def func(self):
        return (82, 20, 92)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'ykmdq'


c = C()
d = c.func()
