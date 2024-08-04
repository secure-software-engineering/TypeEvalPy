# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'nhvwf': 21, 'rckbz': 22, 'goqpi': 58}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return 91


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
