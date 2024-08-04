# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return 11.9


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return (55, 56, 98)


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
