# A simple inheritance scheme.


class A:
    def func(self):
        return 'adzyc'


class B(A):
    pass


b = B()
c = b.func()
