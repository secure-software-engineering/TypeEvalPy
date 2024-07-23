# A class MyClass is defined having nested function call
class MyClass:
    def func(self):
        def nested():
            return {'qnsom': 96, 'fpidw': 12, 'gkuoo': 19}

        return nested()


a = MyClass()
b = a.func()
