# Initialize classes with self parameters in a nested manner.
class C:
    def func(self):
        return {'bigdl': 66, 'qtkjl': 32, 'jente': 67}


class B:
    def __init__(self, c):
        self.c = c

    def func(self):
        return self.c.func()


class A:
    def __init__(self):
        self.c = C()

    def func(self):
        b = B(self.c)
        return b.func()


a = A()
b = a.func()
