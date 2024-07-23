# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return (95, 64, 19)


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return {'ptcll': 56, 'muith': 42, 'bmizc': 9}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
