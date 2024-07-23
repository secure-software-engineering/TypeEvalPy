# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return 97.84


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return {'cqjan': 15, 'xhzqe': 3, 'njoud': 25}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
