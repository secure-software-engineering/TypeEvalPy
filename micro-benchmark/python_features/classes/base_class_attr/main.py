# A class has a base class that is an attribute.
class A:
    class B:
        def bfunc(self):
            return 42


class C(A.B):
    def cfunc(self):
        return "Hello from classC"


c = C()
d=c.cfunc()
e=c.bfunc()