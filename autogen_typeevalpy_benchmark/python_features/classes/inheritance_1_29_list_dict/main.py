# Calling methods of inherited class
class MyClass:
    def func(self):
        return [68, 14, 83]


class MySubClass(MyClass):
    def sub_func(self):
        return {'xfplk': 58, 'radmy': 77, 'kwxla': 58}


a = MySubClass()
b = a.func()
c = a.sub_func()
