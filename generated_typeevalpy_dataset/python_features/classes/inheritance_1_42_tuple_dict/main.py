# Calling methods of inherited class
class MyClass:
    def func(self):
        return (83, 4, 15)


class MySubClass(MyClass):
    def sub_func(self):
        return {'rvwen': 63, 'ngikm': 63, 'spiwd': 10}


a = MySubClass()
b = a.func()
c = a.sub_func()
