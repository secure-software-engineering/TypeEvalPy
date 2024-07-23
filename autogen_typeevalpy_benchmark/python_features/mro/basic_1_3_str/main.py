# A simple inheritance scheme.


class A:
    def func(self):
        return 'dcetv'


class B(A):
    pass


b = B()
c = b.func()
