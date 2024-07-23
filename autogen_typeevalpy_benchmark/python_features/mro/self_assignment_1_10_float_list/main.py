# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return 69.14


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return [56, 37, 34]


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
