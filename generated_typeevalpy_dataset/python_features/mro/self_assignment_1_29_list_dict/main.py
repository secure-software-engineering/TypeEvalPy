# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return [51, 1, 67]


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return {'evezw': 40, 'ydpks': 81, 'sdifq': 56}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
