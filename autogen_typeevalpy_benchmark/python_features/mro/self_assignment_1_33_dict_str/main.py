# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'dvtqg': 72, 'kguld': 71, 'oecrt': 23}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return 'yvkdt'


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
