# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [67, 43, 82]


class B:
    def func(self):
        return (72, 57, 51)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'lesmt'


c = C()
d = c.func()
