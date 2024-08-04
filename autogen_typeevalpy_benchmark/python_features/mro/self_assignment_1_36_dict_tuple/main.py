# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'edjuh': 57, 'sibia': 7, 'sojcx': 48}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return (79, 82, 34)


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
