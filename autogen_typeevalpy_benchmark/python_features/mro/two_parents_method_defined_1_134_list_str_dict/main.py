# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [15, 48, 60]


class B:
    def func(self):
        return 'xxvnp'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'zzncy': 70, 'hroiv': 47, 'brzhy': 63}


c = C()
d = c.func()
