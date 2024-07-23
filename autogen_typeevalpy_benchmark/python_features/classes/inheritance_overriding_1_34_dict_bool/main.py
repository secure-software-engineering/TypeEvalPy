# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'toekk': 21, 'dqxqt': 5, 'wcwzm': 48}


class MySubClass(MyClass):
    def func(self):
        return False


a = MySubClass()
b = a.func()
