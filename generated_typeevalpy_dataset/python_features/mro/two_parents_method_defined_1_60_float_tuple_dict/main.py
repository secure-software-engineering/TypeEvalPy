# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 51.62


class B:
    def func(self):
        return (32, 59, 61)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'yhrjy': 81, 'ocsin': 99, 'zibug': 76}


c = C()
d = c.func()
