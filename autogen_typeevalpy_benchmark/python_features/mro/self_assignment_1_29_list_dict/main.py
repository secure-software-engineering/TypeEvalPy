# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return [59, 40, 11]


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return {'xhvdj': 63, 'vixzd': 25, 'pvdmp': 90}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
