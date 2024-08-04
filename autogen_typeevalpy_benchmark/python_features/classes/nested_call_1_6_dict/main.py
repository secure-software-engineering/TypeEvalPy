# A class MyClass is defined having nested function call
class MyClass:
    def func(self):
        def nested():
            return {'ibeap': 54, 'afsgl': 51, 'krmxd': 46}

        return nested()


a = MyClass()
b = a.func()
