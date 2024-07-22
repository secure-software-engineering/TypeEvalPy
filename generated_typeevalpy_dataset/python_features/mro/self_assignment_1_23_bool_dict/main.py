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
        return {'dzgzq': 98, 'vptaq': 97, 'mcsgn': 39}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
