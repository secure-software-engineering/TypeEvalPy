# A class has a base class with an attribute that is accessed from the derived class.
class A:
    class B:
        def __init__(self):
            self.a = {'bjhew': 88, 'wnmjg': 45, 'xunmm': 98}

        def bfunc(self):
            return [6, 16, 88]


class C(A.B):
    def __init__(self):
        super().__init__()

    def cfunc(self):
        return self.a


c = C()
d = c.cfunc()
e = c.bfunc()
