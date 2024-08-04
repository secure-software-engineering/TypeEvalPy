# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (29, 24, 77)


class B:
    def func(self):
        return True


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'vggdt': 55, 'qufsw': 22, 'gxmzu': 94}


c = C()
d = c.func()
