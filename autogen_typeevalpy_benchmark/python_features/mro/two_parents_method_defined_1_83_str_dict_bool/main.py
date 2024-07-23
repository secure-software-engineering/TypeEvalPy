# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 'iuoqx'


class B:
    def func(self):
        return {'xmrts': 94, 'ycmha': 97, 'imkgl': 20}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return True


c = C()
d = c.func()
