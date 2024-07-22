# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [42, 39, 81]


class B:
    def func(self):
        return {'bjfnu': 79, 'haodh': 5, 'nnxaf': 56}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 'mfxfs'


c = C()
d = c.func()
