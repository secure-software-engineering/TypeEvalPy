# A simple inheritance scheme.


class A:
    def func(self):
        return (63, 89, 31)


class B(A):
    pass


b = B()
c = b.func()
