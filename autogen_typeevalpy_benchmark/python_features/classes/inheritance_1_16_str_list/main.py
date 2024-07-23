# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'bsazs'


class MySubClass(MyClass):
    def sub_func(self):
        return [71, 22, 42]


a = MySubClass()
b = a.func()
c = a.sub_func()
