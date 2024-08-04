# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'orvpb'


class MySubClass(MyClass):
    def sub_func(self):
        return {'iazth': 8, 'rwria': 79, 'ioxme': 7}


a = MySubClass()
b = a.func()
c = a.sub_func()
