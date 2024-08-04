# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 52


class B:
    def func(self):
        return (79, 78, 17)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'ylqmd': 90, 'ptasi': 34, 'wbuop': 2}


c = C()
d = c.func()
