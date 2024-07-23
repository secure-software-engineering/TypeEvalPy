# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'qbktt': 82, 'dezkn': 60, 'aqpqi': 79}


class MySubClass(MyClass):
    def sub_func(self):
        return 71


a = MySubClass()
b = a.func()
c = a.sub_func()
