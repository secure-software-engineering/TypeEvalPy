# A function is assigned as an attribute to self.


class B:
    def funcb(self):
        self.smth = self.func

    def func(self):
        return (65, 6, 48)


class A(B):
    def funca(self):
        self.smth = self.func

    def func(self):
        return {'zrfyg': 56, 'cqzyi': 66, 'oqnwp': 26}


a = A()
a.funcb()
b = a.smth()

a.funca()
b = a.smth()
