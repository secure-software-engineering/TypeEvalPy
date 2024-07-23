# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return 'zawrn'


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return {'cchlu': 10, 'ijeid': 81, 'nvdig': 36}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
