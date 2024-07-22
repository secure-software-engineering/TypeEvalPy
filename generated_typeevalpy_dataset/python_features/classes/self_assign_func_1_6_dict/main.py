# A class is assigned as a self item to a class.


class A:
    def func(self):
        return {'ssfjj': 19, 'ccdoa': 80, 'lpqqt': 26}


class B:
    def __init__(self, a):
        self.a = a

    def func(self):
        return self.a.func()


a = A()
b = B(a)
c = b.func()
