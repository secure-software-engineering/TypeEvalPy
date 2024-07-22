# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return 'tissv'


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return {'rtcpy': 84, 'lfjhf': 58, 'jektk': 3}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
