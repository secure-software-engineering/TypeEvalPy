# A simple inheritance scheme.


class A:
    def func(self):
        return 91


class B(A):
    pass


b = B()
c = b.func()
