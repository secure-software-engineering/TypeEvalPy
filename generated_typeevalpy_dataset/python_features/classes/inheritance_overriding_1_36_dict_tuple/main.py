# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'mqecv': 59, 'xhhcl': 99, 'mqczj': 74}


class MySubClass(MyClass):
    def func(self):
        return (16, 56, 27)


a = MySubClass()
b = a.func()
