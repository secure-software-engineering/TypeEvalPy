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
        return {'pmyci': 8, 'wrsgs': 26, 'hptau': 46}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
