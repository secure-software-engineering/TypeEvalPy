# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (53, 52, 65)


class MySubClass(MyClass):
    def func(self):
        return {'mqwxf': 9, 'wsdyj': 55, 'dktey': 54}


a = MySubClass()
b = a.func()
