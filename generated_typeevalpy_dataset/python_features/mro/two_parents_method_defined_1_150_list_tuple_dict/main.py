# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return [11, 44, 38]


class B:
    def func(self):
        return (69, 48, 8)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'vwczj': 66, 'iiuex': 26, 'jnwjo': 45}


c = C()
d = c.func()
