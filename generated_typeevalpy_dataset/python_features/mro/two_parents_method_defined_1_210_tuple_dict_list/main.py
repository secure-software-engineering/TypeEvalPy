# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (5, 33, 71)


class B:
    def func(self):
        return {'qezmb': 46, 'jmgfa': 26, 'hsiqc': 87}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [29, 78, 56]


c = C()
d = c.func()
