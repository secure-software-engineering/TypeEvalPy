# Two variables are assigned a function in multiple classes with same name via chained assignment


class MyClass:
    def func(self):
        return 42


a = MyClass()
b = a.func
c = b()

class MyClass:
    def func2(self):
        return "Hello from func2 in MyClass"


a = MyClass()
b = a.func2
c = b()

