# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'yunai': 81, 'gmbwy': 18, 'vomgs': 73}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return 42.32


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
