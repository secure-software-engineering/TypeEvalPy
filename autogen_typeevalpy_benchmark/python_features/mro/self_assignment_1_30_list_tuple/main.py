# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return [85, 8, 42]


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return (59, 24, 16)


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
