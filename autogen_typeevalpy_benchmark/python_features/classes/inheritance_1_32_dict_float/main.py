# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'kfpsd': 89, 'twvdh': 12, 'lqeel': 74}


class MySubClass(MyClass):
    def sub_func(self):
        return 17.89


a = MySubClass()
b = a.func()
c = a.sub_func()
