# A simple inheritance scheme.


class A:
    def func(self):
        return 90.54


class B(A):
    pass


b = B()
c = b.func()
