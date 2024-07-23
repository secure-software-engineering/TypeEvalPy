# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'owzyp': 69, 'ohaxu': 82, 'mhuro': 88}


class MySubClass(MyClass):
    def sub_func(self):
        return False


a = MySubClass()
b = a.func()
c = a.sub_func()
