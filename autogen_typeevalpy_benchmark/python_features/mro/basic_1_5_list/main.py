# A simple inheritance scheme.


class A:
    def func(self):
        return [30, 8, 45]


class B(A):
    pass


b = B()
c = b.func()
