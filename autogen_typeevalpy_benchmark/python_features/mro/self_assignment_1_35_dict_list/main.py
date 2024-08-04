# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'fvczm': 25, 'clmrv': 62, 'wrnzt': 70}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return [88, 72, 61]


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
