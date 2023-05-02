# A class B inheriting from A is instantiated.
# On initialization since B doesn't have an `__init__` function, the `__init__` function of A is called.


class A:
    def __init__(self):
        a = 42


class B(A):
    def func(self):
        return "Hello from func"


b = B()
c = b.func()
