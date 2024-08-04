# A class MyClass is defined having nested function call
class MyClass:
    def func(self):
        def nested():
            return (63, 66, 81)

        return nested()


a = MyClass()
b = a.func()
