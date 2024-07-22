# Calling methods of inherited class
class MyClass:
    def func(self):
        return 33


class MySubClass(MyClass):
    def sub_func(self):
        return {'uvzaz': 61, 'phsdy': 70, 'nuvav': 49}


a = MySubClass()
b = a.func()
c = a.sub_func()
