# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (1, 19, 29)


class B:
    def func(self):
        return False


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'nejmy': 88, 'ayydi': 65, 'dogsc': 53}


c = C()
d = c.func()
