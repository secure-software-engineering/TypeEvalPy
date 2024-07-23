# A class MyClass is defined having nested function call
class MyClass:
    def func(self):
        def nested():
            return 3.46

        return nested()


a = MyClass()
b = a.func()
