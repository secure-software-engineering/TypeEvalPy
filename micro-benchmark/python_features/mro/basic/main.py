# A simple inheritance scheme.


class A:
    def func(self):
        return 42


class B(A):
    pass


b = B()
c = b.func()
