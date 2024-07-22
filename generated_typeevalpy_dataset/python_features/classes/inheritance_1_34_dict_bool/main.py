# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'vpvgx': 74, 'imaks': 61, 'wpiin': 49}


class MySubClass(MyClass):
    def sub_func(self):
        return True


a = MySubClass()
b = a.func()
c = a.sub_func()
