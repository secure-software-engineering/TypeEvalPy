# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'weqfs'


class MySubClass(MyClass):
    def sub_func(self):
        return {'mvngf': 88, 'jhxsw': 75, 'kcwln': 61}


a = MySubClass()
b = a.func()
c = a.sub_func()
