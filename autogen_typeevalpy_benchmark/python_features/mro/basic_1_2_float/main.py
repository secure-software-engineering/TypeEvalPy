# A simple inheritance scheme.


class A:
    def func(self):
        return 69.75


class B(A):
    pass


b = B()
c = b.func()
