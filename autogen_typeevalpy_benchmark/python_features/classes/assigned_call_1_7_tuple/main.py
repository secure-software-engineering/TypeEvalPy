# A class is instantiated and we assign one of its functions to a variable and then call that variable.
class MyClass:
    def func(self):
        return (35, 94, 87)


a = MyClass()
b = a.func
b()
