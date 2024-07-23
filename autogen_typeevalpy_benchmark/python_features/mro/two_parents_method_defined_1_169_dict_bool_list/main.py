# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'kakoy': 41, 'lknsy': 87, 'ojlss': 83}


class B:
    def func(self):
        return False


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return [94, 80, 72]


c = C()
d = c.func()
