# A function is assigned as a self attribute.


class A:
    def __init__(self):
        self.smth = self.func2

    def func(self):
        return self.smth()

    def func2(self):
        return <value1>


a = A()
b = a.func()
