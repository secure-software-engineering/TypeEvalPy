# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return [28, 97, 36]


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return {'crbad': 24, 'vbpon': 20, 'rgsmg': 92}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
