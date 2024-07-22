# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'gzahp': 35, 'gbyvm': 79, 'syjnt': 73}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return 60


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
