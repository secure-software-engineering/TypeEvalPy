# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'qikjq': 63, 'iiugq': 18, 'eaxhv': 73}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return True


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
