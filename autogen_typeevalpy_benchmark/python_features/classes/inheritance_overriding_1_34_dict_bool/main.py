# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'hjiyu': 13, 'liddw': 1, 'uxubr': 14}


class MySubClass(MyClass):
    def func(self):
        return False


a = MySubClass()
b = a.func()
