# Calling methods of inherited class
class MyClass:
    def func(self):
        return (41, 12, 52)


class MySubClass(MyClass):
    def sub_func(self):
        return {'ypeoy': 41, 'vjnpm': 68, 'ijkwj': 6}


a = MySubClass()
b = a.func()
c = a.sub_func()
