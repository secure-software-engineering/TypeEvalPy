# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'tffqz': 60, 'gjtwk': 31, 'nnieu': 38}


class MySubClass(MyClass):
    def sub_func(self):
        return 91


a = MySubClass()
b = a.func()
c = a.sub_func()
