# A class has a base class with an attribute that is accessed from the derived class.
class A:
    class B:
        def __init__(self):
            self.a = (45, 46, 49)

        def bfunc(self):
            return {'cqgei': 76, 'cdmbl': 12, 'mqdsu': 90}


class C(A.B):
    def __init__(self):
        super().__init__()

    def cfunc(self):
        return self.a


c = C()
d = c.cfunc()
e = c.bfunc()
