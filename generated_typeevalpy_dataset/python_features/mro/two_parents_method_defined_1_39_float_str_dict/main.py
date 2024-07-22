# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 8.96


class B:
    def func(self):
        return 'bjbhz'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'zmwdo': 8, 'xmcrh': 40, 'vlprd': 94}


c = C()
d = c.func()
