# A class MyClass is defined having nested function call
class MyClass:
    def func(self):
        def nested():
            return (86, 60, 32)

        return nested()


a = MyClass()
b = a.func()
