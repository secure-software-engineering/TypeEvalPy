# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return False


class B:
    def func(self):
        return 'kpmcr'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'fstwt': 1, 'eqdvm': 19, 'kjlyn': 56}


c = C()
d = c.func()
