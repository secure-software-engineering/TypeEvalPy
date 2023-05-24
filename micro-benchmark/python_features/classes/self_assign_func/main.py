# A class is assigned as a self item to a class.


class A:
    def func(self):
        return "Hello from classA"


class B:
    def __init__(self, a):
        self.a = a

    def func(self):
        return self.a.func()


a = A()
b = B(a)
c = b.func()
