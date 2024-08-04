# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return False


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return {'rkpnx': 56, 'ichpg': 4, 'fftwq': 9}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
