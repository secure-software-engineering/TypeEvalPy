# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return 99.8


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return {'boxzh': 80, 'hcune': 70, 'mzqux': 10}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
