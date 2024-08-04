# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'wcgvm': 79, 'slisf': 6, 'wlmhp': 74}


class MySubClass(MyClass):
    def sub_func(self):
        return 98.31


a = MySubClass()
b = a.func()
c = a.sub_func()
