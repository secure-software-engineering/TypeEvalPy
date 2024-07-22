# A simple inheritance scheme.


class A:
    def func(self):
        return 'mzyak'


class B(A):
    pass


b = B()
c = b.func()
