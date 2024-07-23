# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'fqwlu': 26, 'zrrzs': 62, 'rimxh': 57}


class MySubClass(MyClass):
    def sub_func(self):
        return [21, 100, 87]


a = MySubClass()
b = a.func()
c = a.sub_func()
