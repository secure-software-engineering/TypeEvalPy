# Calling methods of inherited class
class MyClass:
    def func(self):
        return 43.58


class MySubClass(MyClass):
    def sub_func(self):
        return {'ibibt': 47, 'zdtpg': 6, 'pggzt': 95}


a = MySubClass()
b = a.func()
c = a.sub_func()
