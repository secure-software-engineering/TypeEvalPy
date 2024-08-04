# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'nmygs': 35, 'nanup': 3, 'awxno': 25}


class MySubClass(MyClass):
    def func(self):
        return (28, 37, 92)


a = MySubClass()
b = a.func()
