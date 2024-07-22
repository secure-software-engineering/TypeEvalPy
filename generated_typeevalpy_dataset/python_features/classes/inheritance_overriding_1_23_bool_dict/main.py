# Method Overriding by imherited class
class MyClass:
    def func(self):
        return False


class MySubClass(MyClass):
    def func(self):
        return {'wbdbo': 30, 'awbim': 63, 'jadha': 17}


a = MySubClass()
b = a.func()
