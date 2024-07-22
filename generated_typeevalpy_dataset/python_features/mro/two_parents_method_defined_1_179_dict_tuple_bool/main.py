# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'asixs': 97, 'pwdpn': 29, 'kqpjo': 9}


class B:
    def func(self):
        return (46, 76, 72)


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return True


c = C()
d = c.func()
