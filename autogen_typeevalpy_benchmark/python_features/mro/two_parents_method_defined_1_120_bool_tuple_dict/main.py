# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return True


class B:
    def func(self):
        return (79, 64, 70)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'xesxe': 63, 'iztuk': 60, 'hjgfd': 10}


c = C()
d = c.func()
