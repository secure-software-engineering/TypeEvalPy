# A class MyClass is defined having nested function call
class MyClass:
    def func(self):
        def nested():
            return [74, 1, 68]

        return nested()


a = MyClass()
b = a.func()
