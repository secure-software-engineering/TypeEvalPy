# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return 88


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return {'rxwwf': 47, 'xfcrc': 51, 'jmbvc': 14}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
