# Calling methods of inherited class
class MyClass:
    def func(self):
        return (52, 64, 3)


class MySubClass(MyClass):
    def sub_func(self):
        return {'mdtvg': 31, 'swhha': 100, 'thujb': 16}


a = MySubClass()
b = a.func()
c = a.sub_func()
