# A simple inheritance scheme.


class A:
    def func(self):
        return (86, 45, 72)


class B(A):
    pass


b = B()
c = b.func()
