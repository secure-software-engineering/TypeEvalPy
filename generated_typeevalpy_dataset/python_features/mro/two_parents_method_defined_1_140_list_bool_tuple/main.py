# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [93, 64, 10]


class B:
    def func(self):
        return False


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (94, 6, 62)


c = C()
d = c.func()
