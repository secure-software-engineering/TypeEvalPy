# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'arcwx': 35, 'betez': 33, 'qiqav': 45}


class MySubClass(MyClass):
    def func(self):
        return [61, 86, 77]


a = MySubClass()
b = a.func()
