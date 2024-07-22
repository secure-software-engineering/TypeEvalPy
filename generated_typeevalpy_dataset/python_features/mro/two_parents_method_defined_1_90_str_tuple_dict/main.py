# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'zximl'


class B:
    def func(self):
        return (36, 63, 40)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'covio': 40, 'svlxn': 58, 'koueg': 84}


c = C()
d = c.func()
