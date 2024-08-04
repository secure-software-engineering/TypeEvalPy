# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'bzxcf': 63, 'bmgje': 16, 'zcefd': 54}


class B:
    def func(self):
        return (18, 77, 75)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [54, 95, 90]


c = C()
d = c.func()
