# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'xaayt': 52, 'phswe': 46, 'hxdlr': 5}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return (53, 51, 100)


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
