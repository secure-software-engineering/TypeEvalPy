# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (12, 58, 14)


class MySubClass(MyClass):
    def func(self):
        return {'pjjlh': 92, 'cogmj': 16, 'amfbo': 22}


a = MySubClass()
b = a.func()
