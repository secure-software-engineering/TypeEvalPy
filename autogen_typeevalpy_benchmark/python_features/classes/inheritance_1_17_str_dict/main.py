# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'tadbs'


class MySubClass(MyClass):
    def sub_func(self):
        return {'koxsv': 39, 'vdrur': 75, 'ebdvc': 47}


a = MySubClass()
b = a.func()
c = a.sub_func()
