# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return (4, 63, 19)


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return [60, 78, 25]


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
