# A simple inheritance scheme.


class A:
    def func(self):
        return True


class B(A):
    pass


b = B()
c = b.func()
