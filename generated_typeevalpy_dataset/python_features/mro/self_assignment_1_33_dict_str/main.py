# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'pcdgz': 66, 'ejdlq': 73, 'iefso': 7}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return 'tuoge'


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
