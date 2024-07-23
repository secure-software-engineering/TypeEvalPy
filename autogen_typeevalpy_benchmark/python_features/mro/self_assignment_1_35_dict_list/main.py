# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'rwswc': 1, 'aytlz': 12, 'wfxhx': 27}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return [97, 16, 41]


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
