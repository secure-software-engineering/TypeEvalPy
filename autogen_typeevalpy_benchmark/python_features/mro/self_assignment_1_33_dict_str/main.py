# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'flkwj': 26, 'urlau': 34, 'auquc': 39}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return 'meufu'


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
