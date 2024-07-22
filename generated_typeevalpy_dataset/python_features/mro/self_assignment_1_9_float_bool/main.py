# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return 64.08


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return False


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
