# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return [63, 87, 16]


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return (67, 79, 71)


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
