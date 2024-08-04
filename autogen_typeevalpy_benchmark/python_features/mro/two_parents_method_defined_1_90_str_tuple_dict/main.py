# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'kldin'


class B:
    def func(self):
        return (70, 49, 46)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'lnutz': 10, 'kwqlb': 93, 'stxaf': 39}


c = C()
d = c.func()
