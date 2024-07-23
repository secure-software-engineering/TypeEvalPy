# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [79, 71, 96]


class B:
    def func(self):
        return {'igvog': 32, 'zvtkj': 10, 'gvkjs': 27}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (66, 80, 45)


c = C()
d = c.func()
