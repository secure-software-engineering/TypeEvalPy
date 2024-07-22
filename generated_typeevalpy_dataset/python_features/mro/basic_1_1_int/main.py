# A simple inheritance scheme.


class A:
    def func(self):
        return 46


class B(A):
    pass


b = B()
c = b.func()
