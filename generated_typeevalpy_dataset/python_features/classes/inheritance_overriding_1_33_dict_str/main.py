# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'pxork': 81, 'mopwf': 75, 'hqpgh': 61}


class MySubClass(MyClass):
    def func(self):
        return 'iovrw'


a = MySubClass()
b = a.func()
