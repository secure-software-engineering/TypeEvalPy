# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (91, 15, 79)


class B:
    def func(self):
        return 61


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'sypln': 25, 'wrxjm': 15, 'ltopg': 42}


c = C()
d = c.func()
