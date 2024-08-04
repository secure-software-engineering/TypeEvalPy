# A class B inheriting from A is instantiated.
# On initialization since B doesn't have an `__init__` function, the `__init__` function of A is called.


class A:
    def __init__(self):
        self.a = {'cevdm': 85, 'ekymr': 58, 'qqwzo': 32}


class B(A):
    def func(self):
        return self.a


b = B()
c = b.func()
