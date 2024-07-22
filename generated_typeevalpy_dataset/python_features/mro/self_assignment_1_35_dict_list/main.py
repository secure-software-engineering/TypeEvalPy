# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'plydh': 26, 'tgtvy': 25, 'efris': 52}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return [62, 24, 84]


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
