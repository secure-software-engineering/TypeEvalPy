# A class method is assigned parameters which are called.
class MyClass:
    def func3(self):
        return 53

    def func2(self, a):
        return a()

    def func1(self, a, b):
        return a(b)


a = MyClass()
d = a.func1(a.func2, a.func3)
