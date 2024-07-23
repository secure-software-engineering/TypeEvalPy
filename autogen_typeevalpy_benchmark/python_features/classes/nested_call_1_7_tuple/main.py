# A class MyClass is defined having nested function call
class MyClass:
    def func(self):
        def nested():
            return (36, 19, 18)

        return nested()


a = MyClass()
b = a.func()
