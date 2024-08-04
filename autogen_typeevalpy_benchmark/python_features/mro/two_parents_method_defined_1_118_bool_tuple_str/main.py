# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return (53, 3, 90)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'ihazt'


c = C()
d = c.func()
