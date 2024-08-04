# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [47, 71, 9]


class MySubClass(MyClass):
    def func(self):
        return {'gzaif': 53, 'djuwt': 15, 'xohij': 41}


a = MySubClass()
b = a.func()
