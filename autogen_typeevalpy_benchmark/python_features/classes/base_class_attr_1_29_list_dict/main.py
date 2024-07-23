# A class has a base class with an attribute that is accessed from the derived class.
class A:
    class B:
        def __init__(self):
            self.a = [73, 53, 53]

        def bfunc(self):
            return {'sthbh': 41, 'mhqyc': 31, 'yyboj': 8}


class C(A.B):
    def __init__(self):
        super().__init__()

    def cfunc(self):
        return self.a


c = C()
d = c.cfunc()
e = c.bfunc()
