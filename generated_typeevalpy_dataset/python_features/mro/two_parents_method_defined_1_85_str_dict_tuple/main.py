# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'ksqen'


class B:
    def func(self):
        return {'qvkpl': 69, 'wjzcf': 6, 'mdskc': 93}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (75, 2, 35)


c = C()
d = c.func()
