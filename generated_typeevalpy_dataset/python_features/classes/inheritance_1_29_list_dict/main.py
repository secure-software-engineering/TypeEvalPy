# Calling methods of inherited class
class MyClass:
    def func(self):
        return [8, 69, 17]


class MySubClass(MyClass):
    def sub_func(self):
        return {'htrkr': 34, 'tyfwo': 18, 'jgqvn': 12}


a = MySubClass()
b = a.func()
c = a.sub_func()
