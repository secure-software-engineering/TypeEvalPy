# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'thcrz': 65, 'iqhfm': 59, 'secrr': 85}


class MySubClass(MyClass):
    def sub_func(self):
        return False


a = MySubClass()
b = a.func()
c = a.sub_func()
