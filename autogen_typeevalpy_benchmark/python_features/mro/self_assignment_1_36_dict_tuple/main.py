# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return {'oowvr': 14, 'kmfek': 29, 'luvwa': 3}


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return (5, 19, 18)


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
