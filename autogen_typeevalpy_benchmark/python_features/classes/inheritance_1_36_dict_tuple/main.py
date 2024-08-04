# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'imevo': 34, 'duvem': 74, 'oqnjq': 87}


class MySubClass(MyClass):
    def sub_func(self):
        return (75, 9, 80)


a = MySubClass()
b = a.func()
c = a.sub_func()
