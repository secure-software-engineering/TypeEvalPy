# A simple inheritance scheme.


class A:
    def func(self):
        return [52, 63, 44]


class B(A):
    pass


b = B()
c = b.func()
