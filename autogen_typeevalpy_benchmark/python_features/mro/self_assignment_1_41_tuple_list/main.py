# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return (19, 18, 68)


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return [9, 82, 62]


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
