# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'niyjn': 84, 'sypcf': 19, 'ehltu': 6}


class B:
    def func(self):
        return (10, 98, 43)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [93, 87, 86]


c = C()
d = c.func()
