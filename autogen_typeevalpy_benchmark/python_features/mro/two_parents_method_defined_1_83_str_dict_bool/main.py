# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'nbwfs'


class B:
    def func(self):
        return {'xafay': 85, 'qvjmk': 56, 'grnnc': 77}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return True


c = C()
d = c.func()
