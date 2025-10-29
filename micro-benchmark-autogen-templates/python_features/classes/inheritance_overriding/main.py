# Method Overriding by imherited class
class MyClass:
    def func(self):
        return <value1>


class MySubClass(MyClass):
    def func(self):
        return <value2>


a = MySubClass()
b = a.func()
MyClass().func()
