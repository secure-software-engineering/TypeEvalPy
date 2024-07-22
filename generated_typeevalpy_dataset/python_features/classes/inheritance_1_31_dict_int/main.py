# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'dnzqf': 92, 'ruekr': 19, 'vzetq': 12}


class MySubClass(MyClass):
    def sub_func(self):
        return 36


a = MySubClass()
b = a.func()
c = a.sub_func()
