# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return 'broib'


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return 86


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
