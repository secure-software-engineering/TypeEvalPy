# A class has a base class with an attribute that is accessed from the derived class.
class A:
    class B:
        def __init__(self):
            self.a = {'kflqp': 92, 'ghqna': 36, 'gzimd': 26}

        def bfunc(self):
            return (26, 89, 55)


class C(A.B):
    def __init__(self):
        super().__init__()

    def cfunc(self):
        return self.a


c = C()
d = c.cfunc()
e = c.bfunc()
