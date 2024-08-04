# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 21


class B:
    def func(self):
        return 'qvmhq'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'ltuvo': 62, 'qptrc': 79, 'xnzpf': 24}


c = C()
d = c.func()
