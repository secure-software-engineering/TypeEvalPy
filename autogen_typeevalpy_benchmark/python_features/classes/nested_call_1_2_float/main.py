# A class MyClass is defined having nested function call
class MyClass:
    def func(self):
        def nested():
            return 86.53

        return nested()


a = MyClass()
b = a.func()
