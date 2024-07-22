# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'zifzu': 34, 'eomjk': 12, 'mtiwf': 51}


class MySubClass(MyClass):
    def sub_func(self):
        return (15, 34, 65)


a = MySubClass()
b = a.func()
c = a.sub_func()
