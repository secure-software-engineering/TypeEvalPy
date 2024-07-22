# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'hoovx': 56, 'vjvgc': 86, 'kicma': 74}


class MySubClass(MyClass):
    def func(self):
        return 65


a = MySubClass()
b = a.func()
