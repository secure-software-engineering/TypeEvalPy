# A simple inheritance scheme.


class A:
    def func(self):
        return 96.31


class B(A):
    pass


b = B()
c = b.func()
