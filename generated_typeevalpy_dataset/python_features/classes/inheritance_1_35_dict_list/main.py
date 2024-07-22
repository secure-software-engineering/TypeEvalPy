# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'xggio': 98, 'troxt': 51, 'mszoo': 34}


class MySubClass(MyClass):
    def sub_func(self):
        return [81, 60, 27]


a = MySubClass()
b = a.func()
c = a.sub_func()
