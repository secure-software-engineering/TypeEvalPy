# A class MyClass is defined having nested function call
class MyClass:
    def func(self):
        def nested():
            return 'kelvq'

        return nested()


a = MyClass()
b = a.func()
