# A class method returns a different class method.


class MyClass:
    def func2(self):
        return [19, 59, 56]

    def func1(self):
        return self.func2


a = MyClass()
b = a.func1()
c = b()
