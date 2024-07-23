# Calling methods of inherited class
class MyClass:
    def func(self):
        return 82


class MySubClass(MyClass):
    def sub_func(self):
        return {'axnpw': 6, 'fmiki': 96, 'fuoop': 30}


a = MySubClass()
b = a.func()
c = a.sub_func()
